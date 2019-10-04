from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template
from .models import DB, User

def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='The space html', users=User.query.all())
    
    return app
