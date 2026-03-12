-- Claim notes journal
-- Run this in Supabase SQL Editor

create table if not exists claim_notes (
  id         uuid primary key default gen_random_uuid(),
  claim_id   uuid references claims(id) on delete cascade not null,
  user_id    uuid references auth.users(id) on delete cascade not null,
  content    text not null,
  created_at timestamptz default now()
);

alter table claim_notes enable row level security;

create policy "Users manage own notes"
  on claim_notes for all
  using  (auth.uid() = user_id)
  with check (auth.uid() = user_id);
