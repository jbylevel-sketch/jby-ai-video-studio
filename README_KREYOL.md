# JBY AI VIDEO STUDIO — Supabase koneksyon (Etap 8)

Etap 8 kontinye apati Etap 7. Frontend HTML, Supabase Auth, pwofil, sis tab yo, RLS, lang HT/FR/EN, lang videyo endepandan, ak mòd `cinematic`, `story`, `both` rete konsève.

## Sa Etap 8 ajoute
- Yon migration lokal `supabase/migrations/20261120000000_jby_initial_schema.sql` ki kopi egzak `schema.sql`, pou Supabase CLI ka prepare menm schema a lokalman.
- `project_id` nan `supabase/config.toml` pou lokal Supabase CLI.
- Yon pgTAP suite `supabase/tests/rls_isolation.test.sql` ki sèvi ak 2 itilizatè tès epi gen 56 assertions: chak kont wè pwòp pwofil/pwojè/pèsonaj/videyo/plan/lyen; chak kont pa ka modifye oswa efase done lòt kont; insert cross-owner bloke; ak trigger ki bloke videyo ki mare ak pwojè lòt kont.
- `tests/verify_stage8.py` verifye migration ak schema pa drift, plan pgTAP la koresponn ak 56 assertions, SQL balanse, epi local config parse.

## Tès lokal Supabase (pa sou production)
Sa mande Docker ak Supabase CLI. Nan rasin pwojè a:

1. `supabase start`
2. `supabase db reset` — sa re-kreye **baz lokal la sèlman** epi aplike migration JBY a. Pa sèvi ak reset sa a sou baz done production.
3. `supabase test db` — kouri pgTAP RLS suite la sou baz lokal la.

Tès la mete fixture itilizatè A/B nan `auth.users`, sèvi ak `set local role authenticated` ak JWT subject, epi li fè rollback. Li pa kreye kont reyèl ni chanje done yon pwojè hosted.

## Pou Supabase Dashboard / hosted
- Egzekite `supabase/schema.sql` nan SQL Editor.
- Egzekite `supabase/verify.sql` epi verifye li fini san erè.
- Mete Project URL ak kle piblik `sb_publishable_...` nan `config.js`; pa mete okenn `sb_secret_...`, `service_role`, kle AI, OAuth oswa peman.
- Deplwaye sèlman `index.html` + `config.js` sou HTTPS.
- Konfigire Auth Site URL/Redirect URLs, epi teste signup/confirmation/login/logout/recovery.
- Fè tès de kont reyèl pou RLS sou pwojè hosted sèlman lè pwojè a pare epi itilizatè a otorize.

## Fichye yo
- `index.html`: frontend miltileng, Auth, recovery, profile, CRUD.
- `config.js`: placeholders Project URL/public key.
- `supabase/schema.sql`: schema hosted/Dashboard.
- `supabase/migrations/20261120000000_jby_initial_schema.sql`: migration local CLI; li dwe rete menm ak schema.sql.
- `supabase/verify.sql`: verifier hosted.
- `supabase/tests/rls_isolation.test.sql`: pgTAP RLS test local (56 assertions).
- `tests/verify_stage8.py`: parity/static checks.
- `tests/run_tests.sh`: lanse tès etap 6–8.

## Limit verifye
- Pa gen Supabase Project URL/key reyèl; config la rete placeholders.
- Migration local ak pgTAP suite pa t egzekite nan anviwònman sa a; Supabase CLI, Docker, PostgreSQL/psql pa disponib.
- SQL verification sou hosted, Auth reyèl, RLS ant kont reyèl ak hosting poko fèt.
- Edge Function toujou starter ki retounen `501 provider_not_configured`.
- AI generation, social publishing, payments, storage upload, admin ak support backend pa aktif.
