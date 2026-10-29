"""Check every bundled Schneider scoring: recompute it through the app's normalise/explain path
and assert the final score matches expected_final_score. No API key needed.

    python3 tools/verify_se_inventory.py
"""
import json
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP))

from geoscore.explain import explain, normalise  # noqa: E402

DIR = APP / "examples" / "se_inventory"


def main():
    index = json.loads((DIR / "index.json").read_text(encoding="utf-8"))
    ok, bad = 0, []
    for e in index:
        judge = normalise(json.loads((DIR / f"{e['id']}.json").read_text(encoding="utf-8")))
        r = explain(judge)["result"]
        same = r["final_score"] == e["expected_final_score"] and r["band"] == e["expected_band"]
        if same:
            ok += 1
        else:
            bad.append(f"{e['id']}: got {r['final_score']} {r['band']}, "
                       f"expected {e['expected_final_score']} {e['expected_band']}")
    print(f"{ok}/{len(index)} scorings match the recorded result.")
    for b in bad:
        print("  MISMATCH", b)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
