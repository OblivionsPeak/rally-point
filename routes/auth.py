"""Login, signup, logout routes."""
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from supabase_client import anon_client

bp = Blueprint('auth', __name__)


@bp.get('/login')
def login_page():
    if session.get('user'):
        return redirect(url_for('dashboard.home'))
    return render_template('login.html')


@bp.post('/login')
def login():
    email    = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    try:
        res = anon_client.auth.sign_in_with_password({'email': email, 'password': password})
        session['user']         = {'id': res.user.id, 'email': res.user.email}
        session['access_token'] = res.session.access_token
        return redirect(url_for('dashboard.home'))
    except Exception as e:
        flash('Invalid email or password. Please try again.')
        return render_template('login.html', email=email)


@bp.get('/signup')
def signup_page():
    if session.get('user'):
        return redirect(url_for('dashboard.home'))
    return render_template('signup.html')


@bp.post('/signup')
def signup():
    email    = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm  = request.form.get('confirm', '')

    if password != confirm:
        flash('Passwords do not match.')
        return render_template('signup.html', email=email)
    if len(password) < 8:
        flash('Password must be at least 8 characters.')
        return render_template('signup.html', email=email)

    try:
        res = anon_client.auth.sign_up({'email': email, 'password': password})
        # Auto sign-in after signup
        session['user']         = {'id': res.user.id, 'email': res.user.email}
        session['access_token'] = res.session.access_token if res.session else None
        return redirect(url_for('dashboard.onboarding'))
    except Exception as e:
        flash('Could not create account. That email may already be registered.')
        return render_template('signup.html', email=email)


@bp.get('/logout')
def logout():
    try:
        anon_client.auth.sign_out()
    except Exception:
        pass
    session.clear()
    return redirect(url_for('index'))
