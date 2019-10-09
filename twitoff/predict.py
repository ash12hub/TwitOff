import numpy as np
from sklearn.model_selection import LogisticRegression

from .models import User

def preduct_user(user1_name, user2_name, tweet_text):
    user1 = User.query.filter(User.username == user1_name)
    user2 = User.query.filter(User.username == user2_name)
    user1_embeddings = np.array([tweet.embedding for tweet in user1.tweets])
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
    embeddings = np.vstack([user1_embeddings, user2_embeddings])
    labels = np.concatenate([np.ones(len(user1.tweets)),
                             np.zeros(len(user1.tweets))])
    # log_red = LogisticRegression()
