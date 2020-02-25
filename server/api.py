from server import app as API, db  
from server.models import User, Tweet 
from flask import jsonify, make_response, request
import tweepy
import os 
import dotenv
dotenv.load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('twitter_key'), os.getenv('twitter_secret'))
auth.set_access_token(os.getenv('twitter_access_token'), os.getenv('twitter_access_secret'))

twitter = tweepy.API(auth)


@API.route('/api')
def api_ping():
    responseObject = {
        'status': 'success', 
        'message': 'Welcome to the twitoff API!'
    }
    return make_response(jsonify(responseObject)), 200


@API.route('/api/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        users = User.query.all()
        print(users)
        responseObject = {
            'status': 'success', 
            'data': [user.to_json() for user in users]
        }
        return make_response(jsonify(responseObject)), 200
    elif request.method == 'POST':
        screen_name = request.get_json()['screen_name']
        # user = twitter.get_user(screen_name)
        # tweets = twitter.user_timeline(user['id'])
        test_user = User.query.filter_by(screen_name=screen_name).first()
        tweets = twitter.user_timeline(screen_name)
        if len(tweets) > 0:
            if test_user:
                user = test_user
                user.img = tweets[0].author.profile_image_url
                user.followers = tweets[0].author.followers_count
                user.description = tweets[0].author.description
            else:
                user = User(
                    screen_name=screen_name, 
                    img=tweets[0].author.profile_image_url, 
                    followers=tweets[0].author.followers_count,
                    description=tweets[0].author.description
                )
                db.session.add(user)
            data = []
            print(f"{user.screen_name} has {len(tweets)} tweets.")
            for item in tweets:
                item = Tweet(
                    text=item.text,
                    user_id=user.id
                )
                user.tweets.append(item)
            db.session.commit()
            responseObject = {
                'status': 'success', 
                'data': user.to_json()
            }
            return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                'status': 'failure', 
                'message': 'no tweets from that screen_name'
            }
            return make_response(jsonify(responseObject)), 404
        

@API.route('/api/users/<id>')
def users_by_id(id):
    user = User.query.filter_by(id=id).first()
    if user:
        responseObject = {
            'status': 'success',
            'data': user.to_json_w_tweets()
        }
        return make_response(jsonify(responseObject)), 200
    responseObject = {
        'status': 'failure',
        'message': 'No user with id {}'.format(id)
    }
    return make_response(jsonify(responseObject)), 404
