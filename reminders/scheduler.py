"""Daily background job: remind veterans about stale claims."""
import logging
from datetime import datetime, timezone, timedelta

from apscheduler.schedulers.background import BackgroundScheduler

from supabase_client import svc_client
from reminders.mailer import send_stale_claim_reminder

log = logging.getLogger(__name__)

STALE_DAYS          = 30   # claim is stale after this many days with no update
REMIND_INTERVAL_DAYS = 7   # don't re-remind the same user more than once per week


def check_stale_claims():
    log.info('[reminders] Checking for stale claims...')
    now         = datetime.now(timezone.utc)
    stale_cut   = (now - timedelta(days=STALE_DAYS)).isoformat()
    remind_cut  = (now - timedelta(days=REMIND_INTERVAL_DAYS)).isoformat()

    # Fetch active claims that haven't been touched in 30+ days
    result = (
        svc_client.table('claims')
        .select('id, user_id, condition, updated_at, last_reminded_at')
        .lt('updated_at', stale_cut)
        .not_.in_('status', ['closed', 'decision_made'])
        .execute()
    )

    if not result.data:
        log.info('[reminders] No stale claims.')
        return

    # Group by user, filtering out users reminded recently
    by_user = {}
    for claim in result.data:
        lr = claim.get('last_reminded_at')
        if lr and lr > remind_cut:
            continue                          # reminded too recently, skip
        by_user.setdefault(claim['user_id'], []).append(claim)

    log.info(f'[reminders] Will remind {len(by_user)} veteran(s).')

    for user_id, claims in by_user.items():
        try:
            user_resp = svc_client.auth.admin.get_user_by_id(user_id)
            email     = user_resp.user.email if user_resp and user_resp.user else None
            if not email:
                continue

            conditions = [c['condition'] for c in claims]
            sent       = send_stale_claim_reminder(email, conditions)

            if sent:
                claim_ids = [c['id'] for c in claims]
                svc_client.table('claims') \
                    .update({'last_reminded_at': now.isoformat()}) \
                    .in_('id', claim_ids) \
                    .execute()
                log.info(f'[reminders] Sent reminder to {email} ({len(conditions)} claim(s)).')

        except Exception as e:
            log.error(f'[reminders] Error for user {user_id}: {e}')


def start_reminder_scheduler():
    scheduler = BackgroundScheduler(timezone='UTC')
    # Run every day at 09:00 UTC
    scheduler.add_job(check_stale_claims, 'cron', hour=9, minute=0)
    scheduler.start()
    log.info('[reminders] Scheduler started (daily 09:00 UTC).')
    return scheduler
