from flask import render_template
from . import projects_bp
    
@projects_bp.route('/browse_projects')
def browse_projects():
    return render_template('projects/browse_projects.html')

@projects_bp.route('/create_project')
def create_project():
    return render_template('projects/create_project.html')

@projects_bp.route('/edit_profile/')
def edit_profile():
    return render_template('projects/edit_profile.html')

@projects_bp.route('/manage_team/')
def manage_team():
    return render_template('projects/manage_team.html')

@projects_bp.route('/project_detail/')
def project_detail():
    return render_template('projects/project_detail.html')

