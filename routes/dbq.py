"""DBQ reference guide."""
from flask import Blueprint, render_template
from routes.dashboard import login_required
from data.dbqs import DBQS, get_categories

bp = Blueprint('dbq', __name__)


@bp.get('/dbq')
@login_required
def dbq_guide():
    return render_template('dbq.html', dbqs=DBQS, categories=get_categories())
