"""Bundle the 62 already-scored Schneider test-run judgements into examples/se_inventory/.

Run once (paths are the author's local source folders):

    python3 tools/build_se_inventory.py

It copies each judge JSON and writes examples/se_inventory/index.json with, per scoring:
id, inventory_type, page_type_key, title, url, stage, expected_final_score, expected_band, note.
"""
import csv
import json
import shutil
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
OUT = APP / "examples" / "se_inventory"

PROJECT = Path("/Users/khushboonijhawan/Documents/geo scoring project")
TESTRUN = PROJECT / "8-geo-v2.2" / "test-run"
JUDGE = TESTRUN / "judge"
RESULT = TESTRUN / "result"
CSV = TESTRUN / "v22_vs_prev_vs_v21.csv"
CORPUS = PROJECT / "4-scoring-project-v2.1" / "GEO Elec Project" / "research" / "corpus" / "index.json"

NOTES = {
    "44": "Same URL as #43 (duplicate page in the inventory), scored as a software page.",
    "59_doc": "Scored from the text of the linked PDF, not the landing page.",
    "60_doc": "Scored from the text of the linked PDF, not the landing page.",
}


def main():
    corpus = {int(p["n"]): p for p in json.loads(CORPUS.read_text(encoding="utf-8"))}
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.json"):
        old.unlink()

    index = []
    for row in rows:
        pid = row["id"]
        src = JUDGE / f"{pid}.json"
        if not src.exists():
            raise SystemExit(f"missing judge file {src}")
        shutil.copyfile(src, OUT / f"{pid}.json")
        res = json.loads((RESULT / f"{pid}_result.json").read_text(encoding="utf-8"))
        page = corpus[int(pid.split("_")[0])]
        index.append({
            "id": pid,
            "inventory_type": row["inv_type"],
            "page_type_key": res["page_type_key"],
            "title": page["title"],
            "url": page.get("final_url") or page["url"],
            "stage": res["stage"],
            "expected_final_score": res["final_score"],
            "expected_band": res["band"],
            "note": NOTES.get(pid, ""),
        })

    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    types = sorted({e["inventory_type"] for e in index})
    print(f"wrote {len(index)} scorings, {len(types)} inventory types -> {OUT}")
    for t in types:
        print(f"  {t}: {sum(e['inventory_type'] == t for e in index)}")


if __name__ == "__main__":
    main()
