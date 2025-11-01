from extensions import db
from datetime import datetime
from flask_login import UserMixin
# from models import Message , Project
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text)
    profile_image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # relationships 
    projects = db.relationship('Project', backref='owner', lazy=True, foreign_keys='Project.owner_id')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy=True)
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id', backref='receiver', lazy=True)
    teams = db.relationship('Team', secondary='team_members', back_populates='members')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    # Dashboard helper methods 
    def get_active_projects_count(self):
        """Count active projects owned by user"""
        return len(self.projects)  

    def get_team_members_count(self):
        """Count total team members across all owned projects"""
        total_members = 0
        for project in self.projects:
            if project.team and project.team.members:
                total_members += len(project.team.members)
        return total_members
    
    def get_unread_messages_count(self):
        """Count unread messages for user"""
        from models.message import Message
        return Message.query.filter_by(receiver_id=self.id, is_read=False).count()

    def get_completed_projects_count(self):
        """Count completed projects"""
        # For now, return 0 - you can implement this when you add project status
        return 0

    def get_recent_projects(self, limit=5):
        """Get recent projects owned by user"""
        from models.project import Project
        return Project.query.filter_by(owner_id=self.id).order_by(Project.created_at.desc()).limit(limit).all()

    def get_joined_projects(self):
        """Get projects where user is a team member but not owner"""
        joined_projects = []
        for team in self.teams:
            if team.project and team.project.owner_id != self.id:
                joined_projects.append(team.project)
        return joined_projects

    def __repr__(self):
        return f"<User {self.username}>"
    





    