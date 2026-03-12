-- Migration: add updated_at and last_reminded_at to claims
-- Run this in Supabase SQL Editor

alter table claims
  add column if not exists updated_at       timestamptz default now(),
  add column if not exists last_reminded_at timestamptz;

-- Backfill updated_at from created_at for existing rows
update claims set updated_at = created_at where updated_at is null;

-- Trigger: auto-set updated_at whenever a claim row is updated
create or replace function set_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists claims_set_updated_at on claims;
create trigger claims_set_updated_at
  before update on claims
  for each row execute function set_updated_at();
