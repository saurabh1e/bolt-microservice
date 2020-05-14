from flask import json

from app import celery, redis


@celery.task(name='send_notification')
def send_notification(args):
    print(args)
    print(redis.keys('*'))


@celery.task(name='save_position')
def save_position(data):
    redisKey = 'device_{}'.format(data['device']['id'])

    ignition = True if data['position']['attributes']['ignition'] == True else False
    alarm = data['position']['attributes']['alarm']

    if data['device']['id'] == 10836:
        redis.rpush('fuel_devices', json.dumps({'deviceid': data['device']['id'], 'fuel': data['position']['attributes']['fuel'],
                                                'serverTime': data['position']['serverTime'], 'fixTime': data['position']['fixTime'],
                                                'temp': data['position']['io202'],
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
                'totalDistance', data['position']['attributes']['totalDistance'],
                'lastUpdate', data['device']['lastUpdate'],
                'ignition', ignition,
                'alarm', alarm,
                'pushedtoServer', False,
                'geofenceIds', json.dumps(data['device']['geofenceIds']),
                'posAttr', json.dumps(data['position']['attributes']))
