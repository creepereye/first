from flask_socketio import SocketIO, send
from flask import Flask, render_template,request,url_for,redirect
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('test.html')



app.run(host='0.0.0.0', port=5000)

