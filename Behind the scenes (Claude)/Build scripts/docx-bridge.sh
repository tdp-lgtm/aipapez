#!/usr/bin/env bash
# docx-bridge.sh — round-trip between Word (.docx) and Markdown so the toolkit
# can operate on your prose, and hand edits back as Word track-changes.
#
# Usage:
#   docx-bridge.sh check
#       Report which conversion tools are installed and how to get the rest.
#
#   docx-bridge.sh to-md   <in.docx> [out.md] [--force]
#       Convert a Word draft to clean Markdown for the skills to edit.
#       (Uses --wrap=none so later diffs are line-stable.)
#
#   docx-bridge.sh to-docx <in.md> [out.docx] [--ref <style.docx>] [--force]
#       Convert Markdown back to Word, optionally matching a journal/style
#       reference .docx (fonts, headings, margins). Default output is
#       <in>.from-md.docx — it will NEVER default to the name of your source
#       Word file, and it refuses to overwrite any existing file without
#       --force.
#
#   docx-bridge.sh review <original.(docx|md)> <edited.(docx|md)> [out.docx] [--force]
#       Produce a Word doc with NATIVE TRACKED CHANGES showing every edit,
#       so you accept/reject in Word as usual. Prefers `pandiff`; if it's not
#       installed, falls back to a clean edited.docx + instructions for Word's
#       built-in Compare.
#
# Install on your machine:
#   macOS:    brew install pandoc && npm install -g pandiff
#   Windows:  winget install JohnMacFarlane.Pandoc ; npm install -g pandiff
#   Linux:    sudo apt install pandoc ; npm install -g pandiff
# No package manager? `pip install pypandoc_binary` also works — this script
# finds and uses pypandoc's bundled pandoc automatically.
# (pandiff needs pandoc + Node. LibreOffice is reported by `check` for
# reference but is not used by this script.)

set -euo pipefail

have() { command -v "$1" >/dev/null 2>&1; }

usage() { sed -n '2,34p' "$0"; }

usage_error() { echo "ERROR: $1" >&2; echo >&2; usage >&2; exit 64; }

# If pandoc isn't on PATH, look for pypandoc's bundled binary (the
# `pip install pypandoc_binary` route in docs/SETUP.md) and put it on PATH so
# both we and pandiff (which spawns `pandoc` itself) can use it.
ensure_pandoc_path() {
  have pandoc && return 0
  local py dir
  for py in python3 python; do
    have "$py" || continue
    dir="$("$py" -c 'import os, pypandoc; print(os.path.dirname(pypandoc.get_pandoc_path()))' 2>/dev/null || true)"
    if [ -n "$dir" ] && [ -x "$dir/pandoc" ]; then
      export PATH="$dir:$PATH"
      return 0
    fi
  done
  return 1
}

require_pandoc() {
  ensure_pandoc_path || {
    echo "ERROR: pandoc is required for this." >&2
    echo "Install:  macOS: brew install pandoc | Win: winget install JohnMacFarlane.Pandoc | Linux: sudo apt install pandoc" >&2
    echo "Or:       pip install pypandoc_binary   (this script will find it)" >&2
    exit 1
  }
}

# Refuse to overwrite an existing file unless the caller passed --force.
# Guards the author's drafts: a to-docx round-trip must never silently
# replace the source .docx (CLAUDE.md: "never overwrite the original .docx").
guard_out() {
  local out="$1" force="$2"
  if [ -e "$out" ] && [ "$force" != "yes" ]; then
    echo "ERROR: refusing to overwrite existing file: $out" >&2
    echo "       Pick another output name, or pass --force if you really mean it." >&2
    exit 1
  fi
}

soffice_bin() {
  if have soffice; then echo soffice
  elif have libreoffice; then echo libreoffice
  elif [ -x "/Applications/LibreOffice.app/Contents/MacOS/soffice" ]; then
    echo "/Applications/LibreOffice.app/Contents/MacOS/soffice"
  else echo ""; fi
}

cmd_check() {
  ensure_pandoc_path || true
  echo "Conversion tooling:"
  for t in pandoc pandiff; do
    if have "$t"; then printf "  %-8s installed (%s)\n" "$t" "$(command -v "$t")"
    else printf "  %-8s MISSING\n" "$t"; fi
  done
  local so; so="$(soffice_bin)"
  if [ -n "$so" ]; then printf "  %-8s installed (%s) [detected; not used by this script]\n" "soffice" "$so"
  else printf "  %-8s missing [optional; not used by this script]\n" "soffice"; fi
  echo
  if ! have pandoc; then
    echo "→ Install pandoc (required):  macOS: brew install pandoc | Win: winget install JohnMacFarlane.Pandoc | Linux: sudo apt install pandoc"
    echo "  (or: pip install pypandoc_binary)"
    exit 1
  fi
  if ! have pandiff; then
    echo "→ pandoc is ready. For one-step Word track-changes also install pandiff:  npm install -g pandiff"
    echo "  (without it, `review` still works via Word's built-in Compare — instructions provided)"
  else
    echo "All set — full Word↔Markdown + track-changes round-trip available."
  fi
  exit 0
}

cmd_to_md() {
  [ $# -ge 1 ] || usage_error "to-md needs an input file: to-md <in.docx> [out.md]"
  require_pandoc
  local in="$1"; shift
  local out="" force="no"
  while [ $# -gt 0 ]; do
    case "$1" in
      --force) force="yes"; shift;;
      *) out="$1"; shift;;
    esac
  done
  [ -n "$out" ] || out="${in%.*}.md"
  guard_out "$out" "$force"
  local mediadir="${out%.md}.media"
  pandoc "$in" -o "$out" --wrap=none --extract-media="$mediadir" -t markdown
  echo "Wrote $out  (media → $mediadir/ if any)"
  echo "Note: live Zotero field-code citations may arrive as formatted text."
  echo "      For clean round-tripping keep citations as [@key]; verify with citecheck."
}

cmd_to_docx() {
  [ $# -ge 1 ] || usage_error "to-docx needs an input file: to-docx <in.md> [out.docx] [--ref <style.docx>]"
  require_pandoc
  local in="$1"; shift
  local out="" ref="" force="no"
  while [ $# -gt 0 ]; do
    case "$1" in
      --ref)
        [ $# -ge 2 ] || usage_error "--ref needs a value: --ref <style.docx>"
        ref="$2"; shift 2;;
      --force) force="yes"; shift;;
      *) out="$1"; shift;;
    esac
  done
  # Default output deliberately does NOT collide with a same-named source
  # .docx (paper.md would otherwise default to paper.docx — the original).
  [ -n "$out" ] || out="${in%.*}.from-md.docx"
  guard_out "$out" "$force"
  if [ -n "$ref" ]; then
    pandoc "$in" -o "$out" --reference-doc="$ref"
  else
    pandoc "$in" -o "$out"
  fi
  echo "Wrote $out${ref:+  (styled from $ref)}"
}

cmd_review() {
  [ $# -ge 2 ] || usage_error "review needs two inputs: review <original.(docx|md)> <edited.(docx|md)> [out.docx]"
  local orig="$1" edited="$2"; shift 2
  local out="" force="no"
  while [ $# -gt 0 ]; do
    case "$1" in
      --force) force="yes"; shift;;
      *) out="$1"; shift;;
    esac
  done
  [ -n "$out" ] || out="review-tracked.docx"
  guard_out "$out" "$force"
  if have pandiff; then
    require_pandoc  # pandiff spawns pandoc itself; fail here with a clear message
    # pandiff emits a docx whose diff is encoded as Word tracked changes.
    pandiff "$orig" "$edited" -o "$out"
    echo "Wrote $out — open in Word; edits appear as tracked changes to accept/reject."
    echo "Note: regeneration can mark cosmetic runs (curly quotes, italics) as"
    echo "      changes. If the redline looks noisy, the real edits are still in"
    echo "      there — or use Word's Review → Compare against the original for"
    echo "      a minimal diff."
  else
    echo "pandiff not installed; producing a clean edited .docx instead." >&2
    require_pandoc
    local clean="${out%.docx}-clean.docx"
    guard_out "$clean" "$force"
    case "$edited" in
      *.docx) cp "$edited" "$clean";;
      *) pandoc "$edited" -o "$clean";;
    esac
    echo "Wrote $clean."
    echo
    echo "To get tracked changes in Word without pandiff:"
    echo "  1. Open Word → Review → Compare → Compare…"
    echo "  2. Original document: $orig (convert to .docx first if it's .md)"
    echo "  3. Revised document:  $clean"
    echo "  4. Word generates a redline with full tracked changes."
    echo "Or install pandiff for one-step output:  npm install -g pandiff"
  fi
}

main() {
  local sub="${1:-}"; shift || true
  case "$sub" in
    check)   cmd_check "$@";;
    to-md)   cmd_to_md "$@";;
    to-docx) cmd_to_docx "$@";;
    review)  cmd_review "$@";;
    *) usage; exit 64;;
  esac
}
main "$@"
