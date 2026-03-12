"""
Rally Point — VA Benefits Companion
"""
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, redirect, url_for, session
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# ── Auth routes ───────────────────────────────────────────────────────────────
from routes.auth      import bp as auth_bp
from routes.dashboard import bp as dashboard_bp
from routes.claims    import bp as claims_bp
from routes.assistant import bp as assistant_bp
from routes.cpep      import bp as cpep_bp
from routes.settings  import bp as settings_bp
from routes.vso         import bp as vso_bp
from routes.pact        import bp as pact_bp
from routes.rating_calc import bp as rating_calc_bp
from routes.buddy       import bp as buddy_bp
from routes.nexus       import bp as nexus_bp
from routes.summary     import bp as summary_bp
from routes.dbq         import bp as dbq_bp
from routes.tdiu        import bp as tdiu_bp

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(claims_bp)
app.register_blueprint(assistant_bp)
app.register_blueprint(cpep_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(vso_bp)
app.register_blueprint(pact_bp)
app.register_blueprint(rating_calc_bp)
app.register_blueprint(buddy_bp)
app.register_blueprint(nexus_bp)
app.register_blueprint(summary_bp)
app.register_blueprint(dbq_bp)
app.register_blueprint(tdiu_bp)

# ── Background scheduler ───────────────────────────────────────────────────────
from reminders.scheduler import start_reminder_scheduler
start_reminder_scheduler()


@app.get('/')
def index():
    if session.get('user'):
        return redirect(url_for('dashboard.home'))
    return render_template('landing.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5056))
    app.run(host='0.0.0.0', port=port, debug=False)
