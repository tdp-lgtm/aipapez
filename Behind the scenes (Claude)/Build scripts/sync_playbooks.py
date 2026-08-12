#!/usr/bin/env python3
"""Refresh plain-text mirrors of every playbook .docx in the agent.

Run this FIRST in any agent session, then Read the mirrors (instant) instead of
converting .docx files one by one. The Word documents remain the masters the
author edits; mirrors are generated copies and are safe to regenerate anytime.

Mirrors live at:  Behind the scenes (Claude)/Playbook mirrors/<relative path>.txt
Skipped sources:  anything in Old versions/, Word lock files (~$...), and
                  everything under Behind the scenes (Claude) itself.
A mirror is refreshed only when its source .docx is newer (mtime), so a
no-change run costs under a second. Mirrors whose source .docx has moved or
been superseded are pruned (exact paths only — they are generated artifacts).
"""
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))          # Build scripts
BTS_DIR = os.path.dirname(SCRIPT_DIR)                            # Behind the scenes (Claude)
AGENT = os.path.dirname(BTS_DIR)                                # agent root
MIRRORS = os.path.join(BTS_DIR, "Playbook mirrors")
READ_DOCX = os.path.join(SCRIPT_DIR, "read_docx.py")


def source_docx_files():
    for root, dirs, files in os.walk(AGENT):
        dirs[:] = [d for d in dirs if d not in ("Old versions", "Behind the scenes (Claude)")]
        for f in files:
            if f.endswith(".docx") and not f.startswith("~$"):
                yield os.path.join(root, f)


def main():
    refreshed, fresh, failed = [], 0, []
    sources = {}
    for src in source_docx_files():
        rel = os.path.relpath(src, AGENT)
        dst = os.path.join(MIRRORS, rel + ".txt")
        sources[os.path.abspath(dst)] = src
        # An empty mirror is never "current" — a failed extraction once left a
        # 0-byte mirror that this mtime check kept treating as fresh (16 Jul 2026).
        if (os.path.exists(dst) and os.path.getsize(dst) > 0
                and os.path.getmtime(dst) >= os.path.getmtime(src)):
            fresh += 1
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        try:
            with open(dst, "w") as out:
                subprocess.run(
                    [sys.executable, READ_DOCX, src],
                    stdout=out, stderr=subprocess.DEVNULL, check=True, timeout=120,
                )
            refreshed.append(rel)
        except Exception as e:
            failed.append((rel, str(e)))
            if os.path.exists(dst):
                os.remove(dst)  # never leave a partial mirror

    pruned = []
    if os.path.isdir(MIRRORS):
        for root, dirs, files in os.walk(MIRRORS):
            for f in files:
                p = os.path.abspath(os.path.join(root, f))
                if f.endswith(".txt") and p not in sources:
                    os.remove(p)
                    pruned.append(os.path.relpath(p, MIRRORS))

    print(f"mirrors: {len(refreshed)} refreshed, {fresh} already current, "
          f"{len(pruned)} pruned, {len(failed)} failed")
    for rel in refreshed:
        print(f"  refreshed: {rel}")
    for rel in pruned:
        print(f"  pruned: {rel}")
    for rel, err in failed:
        print(f"  FAILED: {rel} ({err})")


if __name__ == "__main__":
    main()
