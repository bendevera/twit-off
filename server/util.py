from server.models import User 
from sklearn.linear_model import LogisticRegression as lg
import numpy as np 


def predict_user(id_one, id_two, embedding):
    user_one = User.query.filter_by(id=id_one).first()
    user_two = User.query.filter_by(id=id_two).first()
    if user_one is None or user_two is None:
        raise ValueError 
    user_one_embeddings = user_one.embeddings()
    user_two_embeddings = user_two.embeddings()
    embeddings = np.vstack([user_one_embeddings, user_two_embeddings])
    targets = np.concatenate([
        np.zeros(len(user_one_embeddings)), 
        np.ones(len(user_two_embeddings))
    ])
    result_key = {
        0: user_one.screen_name,
        1: user_two.screen_name
    }
    model = lg().fit(embeddings, targets)
    return result_key[model.predict([embedding])[0]]