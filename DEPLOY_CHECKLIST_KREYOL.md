# Checklist deplwaman JBY — Etap 8

## Local database test (anvan hosted)
- [ ] Enstale Docker ak Supabase CLI.
- [ ] `supabase start`.
- [ ] `supabase db reset` sou stack local sèlman; migration JBY a dwe aplike.
- [ ] `supabase test db`; pgTAP RLS suite la dwe pase 56 assertions.
- [ ] Si schema.sql chanje, mete migration la ajou; `tests/verify_stage8.py` dwe pase parity.

## Hosted project
- [ ] Kreye/ouvri Supabase project.
- [ ] Egzekite `supabase/schema.sql` nan SQL Editor.
- [ ] Egzekite `supabase/verify.sql`; pa deploy si li echwe.
- [ ] Pran Project URL ak publishable key `sb_publishable_...`.
- [ ] Mete yo nan `config.js`; pa mete secret/service_role.
- [ ] Pibliye sèlman `index.html` + `config.js` sou hosting HTTPS.
- [ ] Mete `Site URL` ak `Redirect URLs` nan Supabase Auth; verifye email confirmation/recovery.
- [ ] Teste signup, confirmation, login, logout, reset password.
- [ ] Apre config la ranpli, opsyonèlman kouri `python3 tests/live_connection_check.py` (GET-only; li pa teste RLS).
- [ ] Teste de kont tès pou verifye kont B pa ka li, modifye oswa efase done kont A.
- [ ] Teste HT/FR/EN, lang videyo separe, ak mòd cinematic/story/both.

## Limit
Etap 8 pa konekte ni deplwaye sou Supabase hosted. pgTAP suite pa t kouri isit la; tès lokal static/mock sèlman. AI generation, social OAuth/publishing, payment, storage upload pa aktif.
