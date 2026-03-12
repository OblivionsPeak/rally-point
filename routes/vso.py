"""VSO locator — national directory + zip-based link to VA locator."""
from flask import Blueprint, render_template
from routes.dashboard import login_required
from data.vsos import VSOS

bp = Blueprint('vso', __name__)


@bp.get('/vso')
@login_required
def vso_locator():
    return render_template('vso.html', vsos=VSOS)
