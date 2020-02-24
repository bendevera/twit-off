from server import db 


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    tweets = db.relationship("Tweet")


class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
