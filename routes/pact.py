"""PACT Act presumptive condition checker."""
from flask import Blueprint, render_template
from routes.dashboard import login_required

bp = Blueprint('pact', __name__)


@bp.get('/pact')
@login_required
def pact_checker():
    return render_template('pact.html')
