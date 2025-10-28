from extensions import db
from . import team_members

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    # reverse link to users
    members = db.relationship('User', secondary=team_members, back_populates='teams')

    def __repr__(self):
        return f"<Team {self.name}>"
