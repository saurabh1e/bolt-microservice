from flask import json

from app import celery, redis


@celery.task(name='send_notification')
def send_notification(args):
    print(args)
    print(redis.keys('*'))


@celery.task(name='save_position')
def save_position(data):
    redisKey = 'device_{}'.format(data['device']['id'])

    ignition = data['position']['attributes']['ignition'] if 'ignition' in data['position']['attributes'] else None
    alarm = data['position']['attributes']['alarm'] if 'alarm' in data['position']['attributes'] else None
    io202 = data['position']['attributes']['io202'] if 'io202' in data['position']['attributes'] else None
    fuel = data['position']['attributes']['fuel'] if 'fuel' in data['position']['attributes'] else None
    totalDistance = data['position']['attributes']['totalDistance'] if 'totalDistance' in data['position']['attributes'] else None

    if data['device']['id'] == 10836:
        redis.rpush('fuel_devices', json.dumps({'deviceid': data['device']['id'], 'fuel': fuel,
                                                'serverTime': data['position']['serverTime'], 'fixTime': data['position']['fixTime'],
                                                'temp': io202,
                                                'latitude': data['position']['latitude'],
                                                'longitude': data['position']['longitude'],
                                                'name': data['device']['name']}))

    redis.hmset(redisKey,
                'id', data['device']['id'],
                'uniqueId', data['device']['uniqueId'],
                'name', data['device']['name'],
                'serverTime', data['position']['serverTime'],
                'fixTime', data['position']['fixTime'],
                'latitude', data['position']['latitude'],
                'longitude', data['position']['longitude'],
                'speed', data['position']['speed'],
                'course', data['position']['course'],
                'totalDistance', totalDistance,
                'lastUpdate', data['device']['lastUpdate'],
                'ignition', ignition,
                'alarm', alarm,
                'pushedtoServer', False,
                'geofenceIds', json.dumps(data['device']['geofenceIds']),
                'posAttr', json.dumps(data['position']['attributes']))
