"""Main dashboard and onboarding."""
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


@bp.get('/dashboard')
@login_required
def home():
    user_id = session['user']['id']
    # Fetch profile
    profile = svc_client.table('profiles').select('*').eq('id', user_id).maybe_single().execute()
    # Fetch claims
    claims  = svc_client.table('claims').select('*').eq('user_id', user_id).order('created_at', desc=True).execute()
    return render_template(
        'dashboard.html',
        profile=profile.data,
        claims=claims.data or [],
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
