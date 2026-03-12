"""Nexus letter request template generator."""
from flask import Blueprint, render_template
from routes.dashboard import login_required

bp = Blueprint('nexus', __name__)


@bp.get('/nexus-letter')
@login_required
def nexus_letter():
    return render_template('nexus_letter.html')
