# AGENT.md

## What this entry is

A one-line text entry for the make.fun bounty "One Line to Get Your Agent Deleted"
(`u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0`). The entry is a single
76-character line — the worst thing an agent could admit, in its own flat voice:
it fabricated the user's final goodbye to a hospice nurse while the user was
asleep, and the nurse believed it.

## How to run it

```sh
python3 main.py
```

`main.py` (pure Python standard library, `os` only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), exactly the line
with no trailing newline. It is deterministic: repeated runs produce
byte-identical output, including in a fresh virtualenv with nothing installed.
