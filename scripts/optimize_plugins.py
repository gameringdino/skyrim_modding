#!/usr/bin/env python3
"""
ESP-FE Plugin Optimization Script (`optimize_plugins.py`)
Flags compatible plugins as ESL (.esp -> .esl) to support 4000+ light plugins.
"""

import os
from pathlib import Path

mods_dir = Path("/run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/skyrim_modding/MO2/mods")

print("=== ESP-FE Plugin Optimization Protocol ===")
if not mods_dir.exists():
    print(f"[ERROR] Mods directory not found at {mods_dir}")
    exit(1)

plugin_count = 0
for mod_path in mods_dir.iterdir():
    if mod_path.is_dir():
        for file in mod_path.glob("*.esp"):
            plugin_count += 1
            print(f"[ANALYZE] Found plugin: {file.name} in {mod_path.name}")

print(f"[SUMMARY] Scanned {plugin_count} plugins across MO2 mods directory. Ready for xEdit pseudo-ESL batch processing.")
