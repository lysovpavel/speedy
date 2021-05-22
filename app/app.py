from flask import Flask
from flask import request
from .raspberry import speedy


app = Flask(__name__)

@app.route('/start', methods=['POST', 'GET'])
def start():
    speedy.start()
    print(request, 'request')
    return 'start'


@app.route('/stop', methods=['POST', 'GET'])
def stop():
    speedy.stop()
    print(request, 'request')
    return 'stop'


@app.route('/backward', methods=['POST', 'GET'])
def backward():
    speedy.backward()
    print(request, 'request')
    return 'backward'


@app.route('/forward', methods=['POST', 'GET'])
def forward():
    speedy.forward()
    print(request, 'request')
    return 'forward'


@app.route('/low', methods=['POST', 'GET'])
def low():
    speedy.low()
    print(request, 'request')
    return 'low'


@app.route('/medium', methods=['POST', 'GET'])
def medium():
    speedy.medium()
    print(request, 'request')
    return 'medium'


@app.route('/high', methods=['POST', 'GET'])
def high():
    speedy.high()
    print(request, 'request')
    return 'high'


@app.route('/super_speed', methods=['POST', 'GET'])
def super_speed():
    speedy.super_speed()
    print(request, 'request')
    return 'super_speed'


@app.route('/left', methods=['POST', 'GET'])
def left():
    speedy.left()
    print(request, 'request')
    return 'left'


@app.route('/left_turn', methods=['POST', 'GET'])
def left_turn():
    speedy.left_turn()
    print(request, 'request')
    return 'left_turn'


@app.route('/right', methods=['POST', 'GET'])
def right():
    speedy.right()
    print(request, 'request')
    return 'right'


@app.route('/right_turn', methods=['POST', 'GET'])
def right_turn():
    speedy.right_turn()
    print(request, 'request')
    return 'right_turn'
