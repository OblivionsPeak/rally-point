"""Combined VA rating calculator."""
from flask import Blueprint, render_template
from routes.dashboard import login_required

bp = Blueprint('rating_calc', __name__)


@bp.get('/rating-calc')
@login_required
def rating_calc():
    return render_template('rating_calc.html')
