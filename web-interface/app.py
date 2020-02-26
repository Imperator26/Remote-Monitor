from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

from views import index

@app.route('/')
def hello():
    return 'Hello, World!'
