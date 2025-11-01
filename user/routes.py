from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import Project, Message
from extensions import db
from . import user_bp

@user_bp.route('/dashboard')
@login_required
def dashboard():
    # Get user's owned projects - FIXED: use 'projects' instead of 'owned_projects'
    owned_projects = current_user.projects
    
    # Get projects where user is a team member (but not owner)
    joined_projects = current_user.get_joined_projects()
    
    # Calculate stats using helper methods
    active_projects_count = current_user.get_active_projects_count()
    team_members_count = current_user.get_team_members_count()
    messages_count = current_user.get_unread_messages_count()
    completed_projects_count = current_user.get_completed_projects_count()
    
    # Get recent projects
    recent_projects = current_user.get_recent_projects(5)

    return render_template('user/dashboard.html', 
                         user=current_user,
                         owned_projects=owned_projects,
                         joined_projects=joined_projects,
                         active_projects_count=active_projects_count,
                         team_members_count=team_members_count,
                         messages_count=messages_count,
                         completed_projects_count=completed_projects_count,
                         recent_projects=recent_projects)

@user_bp.route('/profile')
@login_required
def profile():
    # Profile page shows user's own information
    return render_template('user/profile.html', user=current_user)

@user_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        # Update user profile information
        current_user.username = request.form.get('username', current_user.username)
        current_user.bio = request.form.get('bio', current_user.bio)
        current_user.email = request.form.get('email', current_user.email)
        
        # Handle profile image upload (basic implementation)
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and file.filename != '':
                # In a real app, you'd save the file and store the path
                current_user.profile_image = f"uploads/{file.filename}"
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('user.profile'))
    
    return render_template('user/edit_profile.html', user=current_user)

# Add a route to view other users' profiles
@user_bp.route('/profile/<int:user_id>')
@login_required
def view_profile(user_id):
    from models import User
    profile_user = User.query.get_or_404(user_id)
    
    # Get user's public projects (projects they own) - FIXED: use 'projects' instead of 'owned_projects'
    public_projects = profile_user.projects
    
    return render_template('user/public_profile.html', 
                         profile_user=profile_user,
                         public_projects=public_projects)

