"""Account settings."""
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from supabase_client import svc_client, anon_client
from routes.dashboard import login_required

bp = Blueprint('settings', __name__)


@bp.get('/settings')
@login_required
def settings():
    user_id = session['user']['id']
    profile = svc_client.table('profiles').select('*').eq('id', user_id).maybe_single().execute()
    return render_template('settings.html', profile=profile.data or {}, email=session['user']['email'])


@bp.post('/settings/profile')
@login_required
def update_profile():
    user_id = session['user']['id']
    svc_client.table('profiles').upsert({
        'id':             user_id,
        'branch':         request.form.get('branch', ''),
        'discharge_type': request.form.get('discharge_type', ''),
        'service_start':  request.form.get('service_start') or None,
        'service_end':    request.form.get('service_end') or None,
        'current_rating': request.form.get('current_rating') or None,
    }).execute()
    flash('Profile updated.')
    return redirect(url_for('settings.settings'))


@bp.post('/settings/password')
@login_required
def change_password():
    new_pw  = request.form.get('new_password', '')
    confirm = request.form.get('confirm_password', '')
    if new_pw != confirm:
        flash('Passwords do not match.')
        return redirect(url_for('settings.settings'))
    if len(new_pw) < 8:
        flash('Password must be at least 8 characters.')
        return redirect(url_for('settings.settings'))
    try:
        token = session.get('access_token')
        anon_client.auth.update_user({'password': new_pw})
        flash('Password updated successfully.')
    except Exception as e:
        flash(f'Could not update password: {e}')
    return redirect(url_for('settings.settings'))


@bp.post('/settings/delete')
@login_required
def delete_account():
    user_id = session['user']['id']
    try:
        # Delete all user data (cascades handle claims/docs/events)
        svc_client.table('profiles').delete().eq('id', user_id).execute()
        svc_client.auth.admin.delete_user(user_id)
        session.clear()
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'Could not delete account: {e}')
        return redirect(url_for('settings.settings'))
