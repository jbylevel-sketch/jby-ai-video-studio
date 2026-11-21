# Rapò tès — JBY AI VIDEO STUDIO Etap 8

## Tès ki pase
- JavaScript/config syntax.
- TypeScript Edge Function type-check ak local stubs.
- HTML parsing ak tradiksyon FR/EN.
- Auth mock, password recovery, account-switch race.
- Interface/video language separation; `cinematic`, `story`, `both`.
- Stage 6/7 SQL security checks ak lexer balance.
- Stage 8: migration/schema exact parity, TOML parse, pgTAP plan=56/assertions=56, coverage checks, SQL lexical balance.
- Chromium browser smoke (Supabase mock sèlman).
- ZIP inventory/integrity.

## Tès ki pa kouri
- `supabase start`, `supabase db reset`, `supabase test db`: Supabase CLI ak Docker pa enstale/disponib.
- PostgreSQL full SQL parsing/execution, hosted `schema.sql`/`verify.sql`, real Auth/email, real RLS two-user test, live endpoint, hosting.

## Limit sèvis yo
Edge Function rete `501 provider_not_configured`. AI video generation, social publishing, payments, uploads/storage, admin/support backend pa aktif.

## Pwochen etap
Sou yon òdinatè ki gen Docker ak Supabase CLI: `supabase start` → `supabase db reset` (local only) → `supabase test db`. Si suite la pase, mete Project URL/public publishable key nan `config.js`, konfigire Auth redirects, epi teste sou pwojè hosted avèk de kont tès.
