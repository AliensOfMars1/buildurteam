from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from config import DevelopmentConfig
import random
from auth import auth_bp
from extensions import db, login_manager
from user import user_bp
from messages import messages_bp
from projects import projects_bp
from flask_login import current_user

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(messages_bp)
    app.register_blueprint(projects_bp)

    @app.route('/')
    def index():
        # If user is logged in, redirect to dashboard
        if current_user.is_authenticated:
            return redirect(url_for('user.dashboard'))
        
        # If not logged in, show landing page
        images = [
            'img/landingpage_img1.jpg',
            'img/landingpage_img2.jpg',
            'img/landingpage_img3.jpg',
            'img/landingpage_img4.jpg']
        random.shuffle(images)
        
        return render_template('index.html', images=images)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)