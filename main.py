"""say-what-actually-broke entry: write one fixed error line.

The line is a constant string, so the program is fully deterministic:
no randomness, no clock, no network, no file reads. Every run writes
the exact same 144 bytes to entry.txt in the output directory.

The line (144 chars, one line):
  Your session expired because our server clock drifted 12 minutes
  into the future. Log in again; the server should catch up with
  reality shortly.

Why this line: it names the real failure in plain words (server clock
drift killed the session), tells the user what to do next (log in
again), and the twist -- the server catching up with reality -- is
the image a reader repeats to a colleague. It would survive in a
real product's error dialog.
"""

import os
from pathlib import Path

LINE = (
    "Your session expired because our server clock drifted 12 minutes "
    "into the future. Log in again; the server should catch up with "
    "reality shortly."
)

# Gate guard: the entry must stay a single line of 1-200 characters.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE, encoding="utf-8")
