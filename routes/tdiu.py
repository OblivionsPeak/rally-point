"""TDIU guide."""
from flask import Blueprint, render_template
from routes.dashboard import login_required

bp = Blueprint('tdiu', __name__)


@bp.get('/tdiu')
@login_required
def tdiu_guide():
    return render_template('tdiu.html')
