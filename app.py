import eventlet
eventlet.monkey_patch()
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_socketio import SocketIO, emit, send
import tweepy
app = Flask(__name__, static_folder="./tom_is_lost_unity/builds/tom_is_lost_build")

auth = tweepy.OAuthHandler("MIjdhsGgxXDf6x42njMNoUGcp", "diqNByAalW57PxaHzHVeTZXVhWlLwOwtVtaKxz8ooaTFWqfG61")
auth.set_access_token("1237176395740196865-VJGXrPrbyWEHTSeHNQivI0VOD1zabo", "gZrIXk5Ijy7W3kjgpiVUeHaGELIk1QTcOMDGJPfVeXcXs")

api = tweepy.API(auth)

# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')


# @socketio.on('connect')
# def handle_message(message):
#     emit('my response', {'data': 'Connected'})

@socketio.on('beep')
def handle_json(json):
    print("received boop!")
    print(json)
    emit('boop', {"a":"b"})

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        print(socketio)
        socketio.emit('boop', {"got a tweet":status.text})
        print("tweet supposedly sent")

# A welcome message to test our server
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/<path:path>")
def static_resp(path):
    return send_from_directory('./tom_is_lost_unity/builds/tom_is_lost_build', path)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    # app.run(threaded=True, port=5000)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    myStream.filter(track=['@tom_is_alone', '@tomisalone2'], is_async=True)
    print("after")
    socketio.run(app)
    print("even after")
    
    