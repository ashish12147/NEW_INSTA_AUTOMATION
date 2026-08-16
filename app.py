#!/usr/bin/env python3
"""Launcher for the @44.o0 automation.

The runtime source is split into small text parts only so the connected GitHub
API can publish the project reliably.  At startup the parts are concatenated
and compiled as one normal Python module.
"""
from pathlib import Path

root = Path(__file__).resolve().parent / "runtime_parts"
parts = sorted(root.glob("app_*.part"))
if not parts:
    raise SystemExit("Runtime source parts are missing")
source = "".join(p.read_text(encoding="utf-8") for p in parts)
exec(compile(source, "app_runtime.py", "exec"), globals(), globals())
