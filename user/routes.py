from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import user_bp

@user_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html', user=current_user)

@user_bp.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html', user=current_user)

@user_bp.route('/edit-profile')
@login_required
def edit_profile():
    return render_template('user/edit_profile.html', user=current_user)