from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_user

def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='TwitOff!', users=User.query.all())

    @app.route('/user', method['POST'])
    @app.route('/user<name>', method['GET'])
    def user(name=None, message=''):
        name - name or request.values['user_name']
        try:
            if request.method == 'POST':
                add_user(name)
                message = f'User {name} successfully added!'
            tweets = User.query.filter(User.name==name).one().tweets
        except Exception as e:
            message = 'Error adding'
            tweets = []
        return render_template('user.html', title=name, tweets=tweets, message=message)
    
    return app
