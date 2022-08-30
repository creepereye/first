from flask_socketio import SocketIO, send
from flask import Flask, render_template,request,url_for,redirect
import os
app = Flask(__name__)
app.secret_key = 'pswd'
socket_io = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template('test.html')


@app.route('/socket.io.js')
def hi():
  return render_template('socket.io.js')


@app.route('/chat', methods=['POST'])
def chat():
  return render_template('chat.html')

@socket_io.on('message')
def requset(message):
  print('message:'+message)
  to_client=dict()
  if message=='new_connect':
    to_client['message']='wellcome'
    to_client['type']='connect'
  else:
    to_client['message']=message
    to_client['type']='normal'
  send(to_client,broadcast=True)

socket_io.run(app, host='0.0.0.0', port=5000, debug=True ,allow_unsafe_werkzeug=True)

