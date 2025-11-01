from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Project, Team
from extensions import db
from .forms import CreateProjectForm
from . import projects_bp

@projects_bp.route('/browse_projects')
def browse_projects():
    projects = Project.query.all()
    return render_template('projects/browse_projects.html', projects=projects)

@projects_bp.route('/create_project', methods=['GET', 'POST'])
@login_required
def create_project():
    form = CreateProjectForm()
    
    if form.validate_on_submit():
        try:
            # Create project
            project = Project(
                title=form.title.data,
                description=form.description.data,
                owner_id=current_user.id
            )
            db.session.add(project)
            
            # Create team for the project
            team = Team(name=f"{form.title.data} Team", project=project)
            db.session.add(team)
            
            db.session.commit()
            
            flash('🎉 Project created successfully!', 'success')
            return redirect(url_for('user.dashboard'))
            
        except Exception as e:
            db.session.rollback()
            flash('Error creating project. Please try again.', 'error')
            print(f"Error creating project: {e}")
    
    return render_template('projects/create_project.html', form=form)

@projects_bp.route('/project_detail/<int:project_id>')
@login_required
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('projects/project_detail.html', project=project)

@projects_bp.route('/edit_project/<int:project_id>')
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.owner_id != current_user.id:
        flash('You can only edit your own projects.', 'error')
        return redirect(url_for('user.dashboard'))
    
    return render_template('projects/edit_project.html', project=project)

@projects_bp.route('/manage_team/<int:project_id>')
@login_required
def manage_team(project_id):
    project = Project.query.get_or_404(project_id)
    if project.owner_id != current_user.id:
        flash('You can only manage teams for your own projects.', 'error')
        return redirect(url_for('user.dashboard'))
    
    return render_template('projects/manage_team.html', project=project)