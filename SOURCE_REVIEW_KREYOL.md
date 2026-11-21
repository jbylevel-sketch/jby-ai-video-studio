# Revizyon sous — Etap 8

## Chanjman
- Ajoute migration local CLI: `supabase/migrations/20261120000000_jby_initial_schema.sql` (kopi egzak `schema.sql`).
- Mete `project_id = "jby-ai-video-studio"` nan `supabase/config.toml` pou konfigirasyon local.
- Ajoute pgTAP suite `supabase/tests/rls_isolation.test.sql` ki simile de itilizatè authenticated; 56 assertions verifye visibility ak cross-user update/delete sou tout user-owned tables, own inserts, ak video/project ownership trigger.
- Ajoute `tests/verify_stage8.py`; runner kounye a verifye migration/schema parity, pgTAP plan, coverage, SQL lexical balance ak TOML.
- Mete README, test report, deployment checklist ak pre-publish instructions ajou.

## Sa pa chanje
`index.html`, `config.js`, Supabase Auth, reset modpas, lang HT/FR/EN, lang videyo endepandan, `cinematic/story/both`, ak Edge Function starter rete menm jan. Pa gen credentials ni koneksyon hosted ki ajoute.

## Limit
pgTAP test suite la pa kouri nan anviwònman sa a paske Supabase CLI, Docker ak PostgreSQL pa disponib. Static tests pa ranplase ekzekisyon pgTAP.
