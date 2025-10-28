from extensions import db

# Association table between users and teams
team_members = db.Table(
    'team_members',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True)
)

from .user import User
from .project import Project
from .message import Message
from .team import Team
