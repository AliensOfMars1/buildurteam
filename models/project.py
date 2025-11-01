from extensions import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # One project can have one team
    team = db.relationship('Team', backref='project', uselist=False)



    # One project can have one team
    team = db.relationship('Team', backref='project', uselist=False)


    def get_team_size(self):
        """Get total team members including owner"""
        if self.team and self.team.members:
            return len(self.team.members) + 1  # +1 for owner
        return 1  # Just the owner



    """Check if user is a member of this project's team"""
    def is_user_member(self, user_id):
        if self.owner_id == user_id:
            return True
        if self.team:
            return user_id in [member.id for member in self.team.members]
        return False

    def __repr__(self):
        return f"<Project {self.title}>"
    



    