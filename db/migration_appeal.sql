-- Appeal pathway tracker
-- Run this in Supabase SQL Editor

alter table claims
  add column if not exists appeal_type        text,
  add column if not exists appeal_filed_date  date,
  add column if not exists appeal_status      text;
