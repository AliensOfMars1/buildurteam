from flask import Flask, render_template
from config import DevelopmentConfig
import random
from auth import auth_bp
from user import user_bp
from messages import messages_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Register Blueprints
    try:
        app.register_blueprint(auth_bp)
    except Exception as e:
        app.logger.error("Failed to register auth blueprint: %s", e)

    try:
        app.register_blueprint(user_bp)
    except Exception as e:
        app.logger.error("Failed to register user blueprint: %s", e)

    try:
        app.register_blueprint(messages_bp)
    except Exception as e:
        app.logger.error("Failed to register messages blueprint: %s", e)

    @app.route('/')
    def index():
        images = [
            'img/landingpage_img1.jpg',
            'img/landingpage_img2.jpg',
            'img/landingpage_img3.jpg',
            'img/landingpage_img4.jpg']
        random.shuffle(images)
        
        return render_template('index.html', images= images)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
