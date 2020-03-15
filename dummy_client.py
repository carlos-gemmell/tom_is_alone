import socketio

# asyncio
sio = socketio.Client()

sio.connect('http://localhost:5000')
# sio.connect('https://tomisalone.herokuapp.com')

sio.emit('beep', {'foo': 'bar'})

@sio.on('boop')
def on_message(data):
    print('I received a message!')