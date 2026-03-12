"""Claim CRUD and detail view."""
from datetime import datetime, timezone
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from supabase_client import svc_client
from routes.dashboard import login_required, _add_deadline
from data.secondaries import get_secondaries
from data.evidence_templates import get_suggestions

bp = Blueprint('claims', __name__)


@bp.get('/claims/new')
@login_required
def new_claim():
    # Pre-fill from query params when coming from condition suggester
    prefill_condition   = request.args.get('condition', '')
    prefill_claim_type  = request.args.get('claim_type', 'initial')
    return render_template('claim_new.html', prefill_condition=prefill_condition, prefill_claim_type=prefill_claim_type)


@bp.post('/claims/new')
@login_required
def create_claim():
    user_id = session['user']['id']
    data = {
        'user_id':      user_id,
        'condition':    request.form.get('condition', '').strip(),
        'claim_type':   request.form.get('claim_type', 'initial'),
        'date_filed':   request.form.get('date_filed') or None,
        'status':       'pending',
        'notes':        request.form.get('notes', '').strip(),
    }
    svc_client.table('claims').insert(data).execute()
    return redirect(url_for('dashboard.home'))


@bp.get('/claims/<claim_id>')
@login_required
def view_claim(claim_id):
    user_id = session['user']['id']
    claim   = svc_client.table('claims').select('*').eq('id', claim_id).eq('user_id', user_id).maybe_single().execute()
    if not claim.data:
        return redirect(url_for('dashboard.home'))
    events     = svc_client.table('claim_events').select('*').eq('claim_id', claim_id).order('created_at').execute()
    docs       = svc_client.table('documents').select('*').eq('claim_id', claim_id).order('created_at').execute()
    secondaries  = get_secondaries(claim.data['condition'])
    claim_data   = _add_deadline(claim.data)
    notes        = svc_client.table('claim_notes').select('*').eq('claim_id', claim_id).order('created_at', desc=True).execute()
    docs_data    = docs.data or []
    suggestions  = get_suggestions(claim.data['condition']) if not docs_data else []
    return render_template('claim_detail.html', claim=claim_data, events=events.data or [], docs=docs_data, secondaries=secondaries, suggestions=suggestions, notes=notes.data or [])


@bp.post('/claims/<claim_id>/status')
@login_required
def update_status(claim_id):
    user_id    = session['user']['id']
    new_status = request.form.get('status', '')
    note       = request.form.get('note', '').strip()
    # Set decision_date when a decision is first recorded
    update_data = {'status': new_status}
    if new_status == 'decision_made':
        update_data['decision_date'] = datetime.now(timezone.utc).isoformat()
    svc_client.table('claims').update(update_data).eq('id', claim_id).eq('user_id', user_id).execute()
    # Log the event
    svc_client.table('claim_events').insert({
        'claim_id': claim_id,
        'status':   new_status,
        'note':     note,
    }).execute()
    return redirect(url_for('claims.view_claim', claim_id=claim_id))


def _touch_claim(claim_id, user_id):
    """Bump updated_at on the claim so doc activity resets the stale reminder timer."""
    svc_client.table('claims') \
        .update({'updated_at': datetime.now(timezone.utc).isoformat()}) \
        .eq('id', claim_id).eq('user_id', user_id).execute()


@bp.post('/claims/<claim_id>/docs')
@login_required
def add_doc(claim_id):
    user_id = session['user']['id']
    svc_client.table('documents').insert({
        'claim_id':  claim_id,
        'name':      request.form.get('name', '').strip(),
        'collected': False,
    }).execute()
    _touch_claim(claim_id, user_id)
    return redirect(url_for('claims.view_claim', claim_id=claim_id))


@bp.post('/claims/<claim_id>/docs/bulk')
@login_required
def add_docs_bulk(claim_id):
    user_id = session['user']['id']
    names = request.form.getlist('names')
    rows  = [{'claim_id': claim_id, 'name': n.strip(), 'collected': False} for n in names if n.strip()]
    if rows:
        svc_client.table('documents').insert(rows).execute()
        _touch_claim(claim_id, user_id)
    return redirect(url_for('claims.view_claim', claim_id=claim_id))


@bp.post('/claims/<claim_id>/docs/<doc_id>/toggle')
@login_required
def toggle_doc(claim_id, doc_id):
    user_id = session['user']['id']
    doc = svc_client.table('documents').select('collected').eq('id', doc_id).maybe_single().execute()
    if doc.data:
        svc_client.table('documents').update({'collected': not doc.data['collected']}).eq('id', doc_id).execute()
        _touch_claim(claim_id, user_id)
    return redirect(url_for('claims.view_claim', claim_id=claim_id))


@bp.post('/claims/<claim_id>/notes')
@login_required
def add_note(claim_id):
    user_id = session['user']['id']
    content = request.form.get('content', '').strip()
    if content:
        svc_client.table('claim_notes').insert({
            'claim_id': claim_id,
            'user_id':  user_id,
            'content':  content,
        }).execute()
    return redirect(url_for('claims.view_claim', claim_id=claim_id))


@bp.post('/claims/<claim_id>/notes/<note_id>/delete')
@login_required
def delete_note(claim_id, note_id):
    user_id = session['user']['id']
    svc_client.table('claim_notes').delete().eq('id', note_id).eq('user_id', user_id).execute()
    return redirect(url_for('claims.view_claim', claim_id=claim_id))


@bp.get('/claims/<claim_id>/denial')
@login_required
def denial(claim_id):
    user_id = session['user']['id']
    claim   = svc_client.table('claims').select('*').eq('id', claim_id).eq('user_id', user_id).maybe_single().execute()
    if not claim.data:
        return redirect(url_for('dashboard.home'))
    return render_template('denial.html', claim=claim.data)


@bp.post('/claims/<claim_id>/rating')
@login_required
def update_rating(claim_id):
    user_id = session['user']['id']
    rating  = request.form.get('rating')
    # Fetch current claim to avoid overwriting an existing decision_date
    existing = svc_client.table('claims').select('decision_date').eq('id', claim_id).eq('user_id', user_id).maybe_single().execute()
    update_data = {
        'rating': int(rating) if rating else None,
        'status': 'decision_made',
    }
    if not (existing.data and existing.data.get('decision_date')):
        update_data['decision_date'] = datetime.now(timezone.utc).isoformat()
    svc_client.table('claims').update(update_data).eq('id', claim_id).eq('user_id', user_id).execute()
    return redirect(url_for('claims.denial', claim_id=claim_id))
