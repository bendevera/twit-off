from server import db 


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    screen_name = db.Column(db.String)
    description = db.Column(db.String)
    img = db.Column(db.String) 
    followers = db.Column(db.Integer)
    tweets = db.relationship("Tweet")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.screen_name,
            "description": self.description,
            "img": self.img,
            "followers": self.followers
        }
    
    def to_json_w_tweets(self):
        return {
            "id": self.id,
            "name": self.screen_name,
            "description": self.description,
            "img": self.img,
            "followers": self.followers,
            "tweets": [tweet.to_json() for tweet in self.tweets]
        }

    def embeddings(self):
        return [tweet.embedding for tweet in self.tweets]


class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    embedding = db.Column(db.PickleType)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_json(self):
        return {
            "id": self.id,
            "text": self.text
        }
