#!/bin/sh
set -eu
python3 tests/verify_project.py
python3 tests/verify_stage6.py
python3 tests/verify_stage7.py
python3 tests/browser_smoke.py
python3 tests/verify_stage8.py
