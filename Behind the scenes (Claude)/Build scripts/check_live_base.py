#!/usr/bin/env python3
"""Fresh-base guard for paper deliverables.

The failure this prevents (a real incident): the agent rebuilt a draft from a
stale working directory while the author had silently edited the live .docx (no
tracked changes), so two delivered versions dropped six author edits. Rule: the
agent RECORDS a hash at every delivery, and CHECKS
the live file against that record before building on it. Any mismatch means the
author (or Word) touched the file: re-unpack the live file, text-diff against
the last delivered state, and reconcile before proceeding.

Usage (agent-only; never something the author runs):
  python3 check_live_base.py record "<path/to/delivered.docx>"
  python3 check_live_base.py check  "<path/to/live.docx>"

Exit codes for `check`: 0 = matches last recorded delivery (safe base);
1 = MISMATCH (author edits suspected — reconcile first); 2 = no record for
this file (record at next delivery; treat the file as possibly author-touched).

The log is `.delivered_hashes.jsonl`, hidden, next to the file, one JSON line
per delivery: {ts, file, sha256, size}. Keyed by basename, so version renames
get fresh entries and old entries stay as history.
"""
import hashlib
import json
import os
import sys
from datetime import datetime


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_path(path):
    return os.path.join(os.path.dirname(os.path.abspath(path)), ".delivered_hashes.jsonl")


def read_log(path):
    lp = log_path(path)
    if not os.path.exists(lp):
        return []
    entries = []
    with open(lp, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return entries


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("record", "check"):
        print(__doc__)
        sys.exit(2)
    mode, path = sys.argv[1], sys.argv[2]
    if not os.path.exists(path):
        print(f"ERROR: no such file: {path}")
        sys.exit(2)
    digest = sha256(path)
    base = os.path.basename(path)

    if mode == "record":
        entry = {
            "ts": datetime.now().isoformat(timespec="seconds"),
            "file": base,
            "sha256": digest,
            "size": os.path.getsize(path),
        }
        with open(log_path(path), "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"RECORDED {base} sha256={digest[:16]}… at {entry['ts']}")
        sys.exit(0)

    # check
    matches = [e for e in read_log(path) if e.get("file") == base]
    if not matches:
        print(f"NO RECORD for {base} — treat as possibly author-touched; "
              f"text-diff against the last state you know before building on it.")
        sys.exit(2)
    last = matches[-1]
    if last["sha256"] == digest:
        print(f"CLEAN — {base} matches the delivery recorded at {last['ts']}. Safe base.")
        sys.exit(0)
    print(f"MISMATCH — {base} differs from the delivery recorded at {last['ts']}.")
    print("The author (or Word) touched this file. Before building on it:")
    print("  1. re-unpack THIS live file (never a working copy from earlier in the session);")
    print("  2. pandoc both states to text and diff — treat EVERY difference as an author edit")
    print("     (authors often edit with no tracked changes, so 0 w:ins/w:del proves nothing);")
    print("  3. reconcile per the AUTHOR-ROUND PROTOCOL, then record the next delivery.")
    sys.exit(1)


if __name__ == "__main__":
    main()
