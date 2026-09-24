"""Make a reading copy of a draft: title + body, with (verify — #N) placeholder tags stripped.
Usage: python3 Scrap/make_reading_copy.py "WIP Docs/Drafts/Draft vX.Y.md" out.md
The working draft keeps its tags; reading copies are for readers only (cold reader, custodian, referees)."""
import re, sys
src, out = sys.argv[1], sys.argv[2]
t = open(src).read()
title = t.splitlines()[0]
b = t[t.index("## 1."):]
b = re.sub(r"\s*\(verify — #\d+\)", "", b)          # standalone tag
b = re.sub(r";\s*verify — #\d+\)", ")", b)          # "(X 2020; verify — #1)"
b = re.sub(r",\s*verify — #\d+\)", ")", b)          # "(X 1797, 6:237, verify — #20)"
b = re.sub(r";\s*verify — #\d+;", ";", b)           # tag mid-parenthesis
b = re.sub(r";\s*verify\)", ")", b)                 # "(...; verify)"
assert "verify" not in b and "()" not in b, "stripping left an artifact"
open(out, "w").write(title + "\n\n" + b)
print("reading copy:", out, len(b.split()), "words")
