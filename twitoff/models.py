"""SQLAlechemy models for TwitOff"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we query and store historical tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(15), unique=True, nullable=False)
    followers = DB.Column(DB.BigInteger, nullable=False)
    # Tweets IOs are ordinal ints, so we can fetch most recent tweets
    recent_tweet_id = DB.Column(DB.BigInteger, nullable=False)

class Tweets(DB.Model):
    """Stores Tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(208))
    embedded = DB.Column(DB.PickleType, nullable=False)
