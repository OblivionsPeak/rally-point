"""Main dashboard and onboarding."""
from datetime import datetime, timezone, timedelta
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from supabase_client import svc_client
from functools import wraps

bp = Blueprint('dashboard', __name__)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('auth.login_page'))
        return f(*args, **kwargs)
    return decorated


def _add_deadline(claim: dict) -> dict:
    """Attach deadline_days, deadline_date, deadline_urgency to a decided claim."""
    if claim.get('status') != 'decision_made' or not claim.get('decision_date'):
        return claim
    try:
        dd  = datetime.fromisoformat(claim['decision_date'].replace('Z', '+00:00'))
        end = dd + timedelta(days=365)
        days_left = (end - datetime.now(timezone.utc)).days
        claim['deadline_date']    = end.strftime('%b %d, %Y')
        claim['deadline_days']    = days_left
        if days_left < 0:
            claim['deadline_urgency'] = 'expired'
        elif days_left <= 30:
            claim['deadline_urgency'] = 'urgent'
        elif days_left <= 90:
            claim['deadline_urgency'] = 'warning'
        else:
            claim['deadline_urgency'] = 'safe'
    except Exception:
        pass
    return claim


@bp.get('/dashboard')
@login_required
def home():
    user_id = session['user']['id']
    profile = svc_client.table('profiles').select('*').eq('id', user_id).maybe_single().execute()
    claims  = svc_client.table('claims').select('*').eq('user_id', user_id).order('created_at', desc=True).execute()
    claims_data = [_add_deadline(c) for c in (claims.data or [])]
    return render_template(
        'dashboard.html',
        profile=profile.data,
        claims=claims_data,
    )


@bp.get('/onboarding')
@login_required
def onboarding():
    return render_template('onboarding.html')


@bp.post('/onboarding')
@login_required
def onboarding_save():
    user_id = session['user']['id']
    data = {
        'id':             user_id,
        'branch':         request.form.get('branch', ''),
        'discharge_type': request.form.get('discharge_type', ''),
        'service_start':  request.form.get('service_start') or None,
        'service_end':    request.form.get('service_end') or None,
        'current_rating': request.form.get('current_rating') or None,
    }
    svc_client.table('profiles').upsert(data).execute()
    return redirect(url_for('dashboard.home'))
