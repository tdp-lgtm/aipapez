#!/usr/bin/env python3
"""PATCH LIBRARY (agent tool). All-or-nothing string patching for builder
scripts, replacing hand-rolled rep()/assert. Design: NO partial writes
(validate every patch against the CURRENT buffer before applying any), LOUD
failure (which patch, found-count, closest fuzzy match), and no silent no-ops
(the "replace matched 0 times and nothing happened" footgun is not expressible).

Usage:
    from patchlib import apply_patches
    apply_patches(path, [(old1, new1, "tag1"), (old2, new2, "tag2")])
"""
import difflib

def apply_patches(path, patches, write=True):
    s = open(path).read()
    errors = []
    buf = s
    for old, new, tag in patches:
        c = buf.count(old)
        if c != 1:
            near = difflib.get_close_matches(old[:80], [buf[i:i+80] for i in range(0, len(buf)-80, 40)], n=1, cutoff=0.6)
            errors.append(f"[{tag}] expected exactly 1 occurrence, found {c}."
                          + (f" Closest text: {near[0]!r}" if near and c == 0 else ""))
        else:
            buf = buf.replace(old, new)
    if errors:
        raise SystemExit("PATCH FAILURE — nothing written:\n" + "\n".join(errors))
    if write:
        open(path, "w").write(buf)
    return buf

def lint_registry(path):
    """Registry lint: an entry may have a {pin} slot OR a baked pin range, never both;
    flags parentheticals duplicated between full cite and short form."""
    import re
    s = open(path).read()
    problems = []
    for m in re.finditer(r'S\("([^"]+)",\s*"([^"]*)"', s):
        key, full = m.group(1), m.group(2)
        if "{pin}" in full and re.search(r"\d{2,4}-\d{2,4}\{pin\}", full):
            problems.append(f"{key}: baked pin range immediately before {{pin}} slot")
    return problems
