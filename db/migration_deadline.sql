-- Migration: add decision_date to claims for appeal deadline tracking
-- Run this in Supabase SQL Editor

alter table claims
  add column if not exists decision_date timestamptz;

-- Backfill decision_date from claim_events for existing decided claims
update claims c
set decision_date = (
  select min(e.created_at)
  from claim_events e
  where e.claim_id = c.id
    and e.status = 'decision_made'
)
where c.status = 'decision_made'
  and c.decision_date is null;
