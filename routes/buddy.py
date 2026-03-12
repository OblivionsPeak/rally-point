"""Buddy statement template generator."""
from flask import Blueprint, render_template
from routes.dashboard import login_required

bp = Blueprint('buddy', __name__)


@bp.get('/buddy-statement')
@login_required
def buddy_statement():
    return render_template('buddy_statement.html')
