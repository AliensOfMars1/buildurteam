from flask import Flask, render_template
from config import DevelopmentConfig
import random

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

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
