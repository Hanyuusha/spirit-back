from aiohttp import web
import socketio

ROOM = 'room'

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

USER_ROOMS = {}


@sio.event
async def connect(sid, environ):
    room_id = environ['aiohttp.request'].query.get('room', ROOM)
    sio.enter_room(sid, ROOM)
    await sio.emit('ready', to=sid)


@sio.event
def disconnect(sid):
    room = USER_ROOMS.pop(sid)
    sio.leave_room(sid, ROOM)


@sio.event
async def register(sid, payload):
    room = USER_ROOMS[sid]
    await sio.emit('register', data=payload, room=ROOM, skip_sid=sid)


@sio.event
async def webrtc(sid, payload):
    room = USER_ROOMS[sid]
    await sio.emit('webrtc', data=payload, room=ROOM, skip_sid=sid)


if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=9999)
