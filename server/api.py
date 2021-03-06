from server import app as API, db  
from server.models import User, Tweet 
from server.util import predict_user
from flask import jsonify, make_response, request, send_from_directory
import tweepy
import basilica
from threading import Thread
import os 
import dotenv
dotenv.load_dotenv()

TWITTER_KEY = os.getenv('twitter_key')
TWITTER_SECRET = os.getenv('twitter_secret')
TWITTER_ACCESS_TOKEN = os.getenv('twitter_access_token')
TWITTER_ACCESS_SECRET = os.getenv('twitter_access_secret')

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
twitter = tweepy.API(auth)

BASILICA_KEY = os.getenv('basilica_key')


def get_sentence_vector(sentence):
    with basilica.Connection(BASILICA_KEY) as c:
        embedding = c.embed_sentence(sentence, model='twitter')
        # if saving
        # filename = EMB_DIR+text_class+'-'+str(cell['index'])+'.emb'
        # print(f"Saving {filename} | {text_class} | {cell['index']}")
        # with open(filename, 'w') as f:
        #     f.write(json.dumps(embedding))
        return embedding

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# Serve React App
@API.route('/', defaults={'path': ''})
@API.route('/<path:path>')
def serve(path):
    print(BASE_PATH + '/' + 'build/' + path)
    if path != "" and os.path.exists(BASE_PATH + '/' + 'build/' + path):
        print("SENDING OTHER")
        return send_from_directory(os.path.join(BASE_PATH, 'build'), path)
    else:
        print("SENDING INDEX")
        print(os.path.join(BASE_PATH, 'index.html'))
        return send_from_directory(os.path.join(BASE_PATH, 'build'), 'index.html')


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
        def grab_tweets(tweets, user_id):
            with API.app_context():
                user = User.query.filter_by(id=user_id).first()
                data = []
                for item in tweets:
                    embedding = get_sentence_vector(item.full_text)
                    item = Tweet(
                        text=item.full_text,
                        embedding=embedding,
                        user_id=user.id
                    )
                    user.tweets.append(item)
                db.session.commit()
                print(f"{user.screen_name} has {len(user.tweets)} tweets.")
        screen_name = request.get_json()['screen_name']
        # user = twitter.get_user(screen_name)
        # tweets = twitter.user_timeline(user['id'])
        test_user = User.query.filter_by(screen_name=screen_name).first()
        twitter_user = twitter.get_user(screen_name)
        tweets = twitter_user.timeline(
            count=50, 
            exclude_replies=True, 
            include_rts=False, 
            tweet_mode='extended'
        )
        # tweets = twitter.user_timeline(screen_name)
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
            db.session.commit()
            responseObject = {
                'status': 'success', 
                'data': user.to_json()
            }
            thread = Thread(target=grab_tweets, kwargs={'tweets': tweets, 'user_id': user.id})
            thread.start()
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


@API.route('/api/predict', methods=['POST'])
def predict():
    payload = request.get_json()
    try: 
        embedding = get_sentence_vector(payload['sentence'])
        user = predict_user(payload['id_one'], payload['id_two'], embedding)
        print(user)
        responseObject = {
            'status': 'success',
            'data': user
        }
        return make_response(jsonify(responseObject)), 200
    except Exception as e:
        print(e)
        responseObject = {
            'status': 'failure',
            'message': str(e)
        }
        return make_response(jsonify(responseObject)), 404