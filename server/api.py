from server import app as API, db  
from server.models import User, Tweet 
from flask import jsonify, make_response 
import tweepy
import os 
import dotenv
dotenv.load_dotenv()

auth = tweepy.OAuthHandler(os.getenv('twitter_key'), os.getenv('twitter_secret'))
auth.set_access_token(os.getenv('twitter_access_token'), os.getenv('twitter_access_secret'))

twitter = tweepy.API(auth)


@API.route('/api')
def api_ping():
    return jsonify({'status': 'success', 'message': 'Welcome to the twitoff API!'})

@API.route('/api/user/<screen_name>')
def api_user(screen_name):
    # user = twitter.get_user(screen_name)
    # tweets = twitter.user_timeline(user['id'])
    tweets = twitter.user_timeline(screen_name)
    data = []
    for item in tweets:
        item = {
            "author_name": item.author.screen_name,
            "author_img": item.author.profile_image_url,
            "author_follow_count": item.author.followers_count,
            "is_initial": item.in_reply_to_status_id,
            "is_quote": item.is_quote_status,
            "text": item.text,
            "favorites": item.favorite_count,
            "retweets": item.retweet_count,
            "created": item.created_at
        }
        data.append(item)
    return jsonify({'status': 'success', 'data': data})
