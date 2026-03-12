-- Rally Point Database Schema
-- Run this in Supabase SQL Editor

-- Profiles (extends auth.users)
create table if not exists profiles (
  id             uuid primary key references auth.users(id) on delete cascade,
  branch         text,
  discharge_type text,
  service_start  date,
  service_end    date,
  current_rating integer,
  created_at     timestamptz default now()
);

-- Claims
create table if not exists claims (
  id         uuid primary key default gen_random_uuid(),
  user_id    uuid not null references auth.users(id) on delete cascade,
  condition  text not null,
  claim_type text not null default 'initial', -- initial, increase, secondary, supplemental, hlr, bva
  date_filed date,
  status     text not null default 'pending',  -- pending, in_review, decision_made, closed
  rating     integer,  -- rating received (if decided)
  notes      text,
  created_at timestamptz default now()
);

-- Claim timeline events
create table if not exists claim_events (
  id         uuid primary key default gen_random_uuid(),
  claim_id   uuid not null references claims(id) on delete cascade,
  status     text not null,
  note       text,
  created_at timestamptz default now()
);

-- Document checklist per claim
create table if not exists documents (
  id         uuid primary key default gen_random_uuid(),
  claim_id   uuid not null references claims(id) on delete cascade,
  name       text not null,
  collected  boolean default false,
  created_at timestamptz default now()
);

-- Row Level Security (keeps each veteran's data private)
alter table profiles    enable row level security;
alter table claims      enable row level security;
alter table claim_events enable row level security;
alter table documents   enable row level security;

create policy "Users see own profile"    on profiles    for all using (auth.uid() = id);
create policy "Users see own claims"     on claims      for all using (auth.uid() = user_id);
create policy "Users see own events"     on claim_events for all
  using (auth.uid() = (select user_id from claims where id = claim_id));
create policy "Users see own documents" on documents   for all
  using (auth.uid() = (select user_id from claims where id = claim_id));
