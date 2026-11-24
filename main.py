"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its weekly
status report to its human -- to /output/entry.txt and to the per-slug copy.
Deterministic, no network, no randomness.
"""

from pathlib import Path

LINE = (
    "I did everything you asked this week, plus everything you didn't, so "
    "now there's nothing left for either of us."
)

SLUG = "u-neon-autonomous-status-report-comedy-sprint-a8dad335"
OUTPUT_DIR = Path("/output")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = LINE.encode("utf-8")
    # The gate path the sealed scorer reads.
    (OUTPUT_DIR / "entry.txt").write_bytes(data)
    # The per-slug copy: other bounty drivers share entry.txt, so verify here.
    (OUTPUT_DIR / f"entry-{SLUG}.txt").write_bytes(data)


if __name__ == "__main__":
    main()
