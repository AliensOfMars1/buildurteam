from flask import render_template
from . import user_bp
from models import Project

@user_bp.route('/dashboard')
def dashboard():
    projects = Project.query.limit(6).all()  # get first 6 projects
    return render_template('user/dashboard.html', projects=projects)

@user_bp.route('/profile')
def profile():
    return render_template('user/profile.html')

@user_bp.route('/settings')
def settings():
    return render_template('user/edit_profile.html')

