"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, offline, standard library only. The joke is fixed text:
every run writes the same bytes.
"""

import os

JOKE = "The agent wrote 2,000 lines I never read, the reviewer approved them in four seconds, and the only honest line in the whole PR was the agent's own comment: 'LGTM.'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
