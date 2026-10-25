import json,csv,glob,os,statistics as st
root='../../4-scoring-project-v2.1/GEO Elec Project/research'
idx={f"{p['n']:02d}":p for p in json.load(open(root+'/corpus/index.json'))}
old={}
for r in csv.reader(open(root+'/final-scoring/SE_GEO_scored_inventory_v2.1.csv',encoding='utf-8-sig')):
    if r and r[0][:2].isdigit():
        try: old[r[0]]=int(float(r[7]))
        except: pass
rows=[]
for f in sorted(glob.glob('result/*_result.json')):
    nid=os.path.basename(f).replace('_result.json','')
    d=json.load(open(f)); base=nid[:2]; p=idx.get(base,{})
    crit=sorted(d['criteria'],key=lambda c:-c.get('impact_points',0))[:3]
    rows.append(dict(id=nid,inv_type=p.get('type',''),title=p.get('title','')[:80],url=p.get('url',''),key=d['page_type_key'],stage=d['stage'],
      score=d['final_score'],band=d['band'],v21=old.get(nid,'' if nid!='44' else 'not scored'),
      gates=';'.join(g if isinstance(g,str) else g.get('id','') for g in d.get('gates_triggered',[])),
      penalties=';'.join(p_ if isinstance(p_,str) else p_.get('id','') for p_ in d.get('penalties',[])),
      gaps='; '.join(f"{c['id']} +{c.get('impact_points',0):.1f}" for c in crit)))
for r in rows: r['diff']=(r['score']-r['v21']) if isinstance(r['v21'],int) else ''
w=csv.DictWriter(open('all_60_results.csv','w',newline=''),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
by={}
for r in rows: by.setdefault(r['inv_type'],[]).append(r)
out=['| Inventory type | Pages | Median new | Median v2.1 | Range new | Bands (P/A/G) | Mean abs diff |','|---|---|---|---|---|---|---|']
for t,rs in by.items():
    s=[r['score'] for r in rs]; o=[r['v21'] for r in rs if isinstance(r['v21'],int)]; dd=[abs(r['diff']) for r in rs if r['diff']!='']
    b=[sum(r['band']==x for r in rs) for x in ('Poor','Average','Good')]
    out.append(f"| {t} | {len(rs)} | {st.median(s)} | {st.median(o) if o else '-'} | {min(s)}–{max(s)} | {b[0]}/{b[1]}/{b[2]} | {round(st.mean(dd),1) if dd else '-'} |")
s=[r['score'] for r in rows];dd=[abs(r['diff']) for r in rows if r['diff']!='']
out.append(f"| **All** | {len(rows)} | {st.median(s)} | {st.median([r['v21'] for r in rows if isinstance(r['v21'],int)])} | {min(s)}–{max(s)} | {sum(r['band']=='Poor' for r in rows)}/{sum(r['band']=='Average' for r in rows)}/{sum(r['band']=='Good' for r in rows)} | {round(st.mean(dd),1)} |")
print('\n'.join(out)); print('within10',sum(x<=10 for x in dd),'of',len(dd))
open('summary_by_type.md','w').write('\n'.join(out))
