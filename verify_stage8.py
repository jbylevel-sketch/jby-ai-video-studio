#!/usr/bin/env python3
"""Stage 8 checks: migration parity and real pgTAP RLS test coverage."""
from pathlib import Path
import re
import tomllib

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = (ROOT / "supabase/schema.sql").read_text(encoding="utf-8")
MIGRATION = (ROOT / "supabase/migrations/20261120000000_jby_initial_schema.sql").read_text(encoding="utf-8")
PGTAP = (ROOT / "supabase/tests/rls_isolation.test.sql").read_text(encoding="utf-8")
CONFIG = tomllib.loads((ROOT / "supabase/config.toml").read_text(encoding="utf-8"))

# Reuse the Stage 7 lexical checker. Importing it also runs its previous assertions.
from verify_stage7 import lexical_balance  # noqa: E402

assert SCHEMA == MIGRATION, "Local migration must match the Dashboard schema SQL"
lexical_balance(PGTAP, "pgTAP RLS test")
plan = re.search(r"select\s+plan\((\d+)\)\s*;", PGTAP, re.I)
assert plan, "pgTAP plan declaration is missing"
expected = int(plan.group(1))
assert expected == 56, f"Expected 56 assertions in this test suite, found plan({expected})"
assert len(re.findall(r"^\s*select\s+(?:is|is_empty|lives_ok|throws_ok)\s*\(", PGTAP, re.I | re.M)) == expected, "pgTAP plan count does not match assertion count"
for table in ("profiles", "projects", "characters", "videos", "daily_plans", "social_links"):
    assert f"public.{table}" in PGTAP, f"RLS test does not mention {table}"
for table, label in (("profiles", "profile"), ("projects", "project"), ("characters", "character"), ("videos", "video"), ("daily_plans", "plan"), ("social_links", "social link")):
    assert f"A cannot read B {label}" in PGTAP and f"B cannot read A {label}" in PGTAP, f"Cross-user read test missing for {table}"
assert "A cannot update B profile" in PGTAP and "A cannot delete B profile" in PGTAP
assert "B cannot update A profile" in PGTAP and "B cannot delete A profile" in PGTAP
for table in ("projects", "characters", "videos", "daily_plans", "social_links"):
    assert re.search(rf"update\s+public\.{table}.*?returning id", PGTAP, re.I | re.S), f"Cross-user update test missing for {table}"
    assert re.search(rf"delete\s+from\s+public\.{table}.*?returning id", PGTAP, re.I | re.S), f"Cross-user delete test missing for {table}"
assert "set local role authenticated" in PGTAP.lower() and "set local request.jwt.claim.sub" in PGTAP.lower(), "Tests must run as authenticated users with JWT subjects"
assert "select * from finish()" in PGTAP.lower() and "rollback" in PGTAP.lower(), "pgTAP result and rollback are missing"
assert CONFIG.get("project_id") == "jby-ai-video-studio", "Local CLI project_id missing"
assert CONFIG.get("functions", {}).get("generate-video", {}).get("verify_jwt") is True, "Edge Function JWT verification must remain enabled"

print("PASS: Stage 8 migration exactly matches schema.sql")
print("PASS: pgTAP test has 56 assertions and lexical balance")
print("PASS: RLS test covers cross-user reads on all six tables and update/delete on all six tables")
print("PASS: authenticated role + JWT subject simulation is included")
print("PASS: Supabase local CLI config is parseable and project id is set")
print("LIMIT: pgTAP suite not executed; Supabase CLI, Docker, and PostgreSQL are unavailable here")
