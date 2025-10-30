from app import create_app
from extensions import db

# Create the app instance
app = create_app()

def init_database():
    with app.app_context():
        # Drop all tables (optional - only for development)
        # db.drop_all()
        
        # Create all tables
        db.create_all()
        print("✅ Database tables created successfully!")
        print("✅ Tables created: users, projects, messages, teams, team_members")

if __name__ == '__main__':
    init_database()