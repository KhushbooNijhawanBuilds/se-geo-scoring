import json,csv,glob,os,statistics as st
R='../../4-scoring-project-v2.1/GEO Elec Project/research'
idx={f"{p['n']:02d}":p for p in json.load(open(R+'/corpus/index.json'))}
old={};ost={}
for r in csv.reader(open(R+'/final-scoring/SE_GEO_scored_inventory_v2.1.csv',encoding='utf-8-sig')):
    if r and r[0][:2].isdigit():
        try: old[r[0]]=int(float(r[7])); ost[r[0]]=r[5]
        except: pass
def load(d,i):
    f=f'{d}/{i}_result.json'
    return json.load(open(f)) if os.path.exists(f) else None
rows=[]
for f in sorted(glob.glob('result/*_result.json')):
    i=os.path.basename(f)[:-12]; n=json.load(open(f)); p=load('../../7-geo-all-types/test-run/result',i)
    crit=sorted(n['criteria'],key=lambda c:-c.get('impact_points',0))[:3]
    rows.append(dict(id=i,inv_type=idx.get(i[:2],{}).get('type',''),title=idx.get(i[:2],{}).get('title','')[:80],key=n['page_type_key'],
      stage_v22=n['stage'],stage_prev=p['stage'] if p else '',stage_v21=ost.get(i,''),
      v22=n['final_score'],band_v22=n['band'],prev=p['final_score'] if p else '',band_prev=p['band'] if p else '',v21=old.get(i,''),
      gates=';'.join(g if isinstance(g,str) else g.get('id','') for g in n.get('gates_triggered',[])),
      top_gaps='; '.join(f"{c['id']} +{c.get('impact_points',0):.1f}" for c in crit)))
w=csv.DictWriter(open('v22_vs_prev_vs_v21.csv','w',newline=''),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def m(x): return round(st.median(x),1) if x else '-'
def mad(a,b): d=[abs(x-y) for x,y in zip(a,b)]; return round(st.mean(d),1)
L=['| Inventory type | n | v2.2 median | prev-run median | v2.1 median | mean |v2.2−prev| | mean |v2.2−v2.1| | v2.2 bands P/A/G |','|---|---|---|---|---|---|---|---|']
by={}
for r in rows: by.setdefault(r['inv_type'],[]).append(r)
for t,rs in list(by.items())+[('**All**',rows)]:
    a=[r['v22'] for r in rs]; pr=[(r['v22'],r['prev']) for r in rs if r['prev']!='']; o=[(r['v22'],r['v21']) for r in rs if r['v21']!='']
    L.append(f"| {t} | {len(rs)} | {m(a)} | {m([y for _,y in pr])} | {m([y for _,y in o])} | {mad(*zip(*pr))} | {mad(*zip(*o))} | {sum(r['band_v22']=='Poor' for r in rs)}/{sum(r['band_v22']=='Average' for r in rs)}/{sum(r['band_v22']=='Good' for r in rs)} |")
pr=[r for r in rows if r['prev']!='']
bc=[r for r in pr if r['band_v22']!=r['band_prev']]
sp=sum(r['stage_v22']!=r['stage_prev'] for r in pr)
big=[f"{r['id']} ({r['v22']-r['prev']:+d})" for r in pr if abs(r['v22']-r['prev'])>10]
d=[r['v22']-r['prev'] for r in pr]
extra=[f"- Pages: {len(rows)}. Mean change v2.2 − previous run: {st.mean(d):+.1f}; within ±10: {sum(abs(x)<=10 for x in d)} of {len(d)}; >10: {', '.join(big)}.",
 f"- Band changes vs previous run: {len(bc)} — "+', '.join(f"{r['id']} {r['band_prev']}→{r['band_v22']}" for r in bc),
 f"- Stage differs from previous run on {sp} of {len(pr)} pages."]
open('comparison_summary.md','w').write('\n'.join(L+['']+extra)); print('\n'.join(L+['']+extra))
