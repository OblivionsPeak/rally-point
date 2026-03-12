"""Printable claim summary for VSO appointments."""
from datetime import datetime, timezone
from flask import Blueprint, render_template, session
from supabase_client import svc_client
from routes.dashboard import login_required, _add_deadline

bp = Blueprint('summary', __name__)


@bp.get('/summary')
@login_required
def claim_summary():
    user_id = session['user']['id']
    profile = svc_client.table('profiles').select('*').eq('id', user_id).maybe_single().execute()
    claims  = svc_client.table('claims').select('*').eq('user_id', user_id).order('created_at', desc=True).execute()

    claims_data = [_add_deadline(c) for c in (claims.data or [])]

    # Fetch all docs for this user's claims in one query
    claim_ids = [c['id'] for c in claims_data]
    docs_by_claim = {}
    if claim_ids:
        docs = svc_client.table('documents').select('*').in_('claim_id', claim_ids).execute()
        for doc in (docs.data or []):
            docs_by_claim.setdefault(doc['claim_id'], []).append(doc)

    # Attach docs to each claim
    for c in claims_data:
        c['docs'] = docs_by_claim.get(c['id'], [])
        c['docs_total']     = len(c['docs'])
        c['docs_collected'] = sum(1 for d in c['docs'] if d['collected'])

    now = datetime.now(timezone.utc).strftime('%B %d, %Y')
    return render_template(
        'claim_summary.html',
        profile=profile.data or {},
        claims=claims_data,
        email=session['user']['email'],
        now=now,
    )
