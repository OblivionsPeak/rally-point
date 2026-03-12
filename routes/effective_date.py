"""Effective date explainer guide."""
from flask import Blueprint, render_template
from routes.dashboard import login_required

bp = Blueprint('effective_date', __name__)


@bp.get('/effective-date')
@login_required
def effective_date_guide():
    return render_template('effective_date.html')
