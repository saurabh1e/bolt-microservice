from app import celery, redis


@celery.task(name='send_notification')
def send_notification(args):
    print(args)
    print(redis.keys('*'))


@celery.task(name='save_position')
def save_position(data):
    print(data)
    print(redis.keys('*'))

    redisKey = data['device']['id'].format()

    # ${body.device.id}
    # let ignition = (body.position.attributes.ignition == true ) ? "true": ((body.position.attributes.ignition == false) ?"false" : "null");
    # let alarm = (body.position.attributes.alarm) ? body.position.attributes.alarm : "null";
    #
    # if (body.device.id === 13460 || body.device.id === 19897 || body.device.id === 137) {
    #     // console.log("body.device",JSON.stringify(body));
    # }
    # if(body.device.id === 10836){
    #     client.rpush(['fuel_devices',JSON.stringify({deviceid:body.device.id,fuel:body.position.attributes.fuel,serverTime:body.position.serverTime,fixTime:body.position.fixTime,temp:body.position.io202,latitude:body.position.latitude,longitude:body.position.longitude,name:body.device.name})], function(err, reply) {
    #         // console.log(reply); //prints 2
    #     });
    #
    #     // client.lrange('jsonlist', 0, -1, function(err, reply) {
    #     //     // console.log('list reply',reply); // ['angularjs', 'backbone']
    #     // });
    # }
    # // console.log('body.position',body.position)
    #
    # client.hmset(redisKey,
    #     'id', body.device.id,
    #     'uniqueId', body.device.uniqueId,
    #     'name', body.device.name,
    #     'serverTime', body.position.serverTime,
    #     'fixTime', body.position.fixTime,
    #     'latitude', body.position.latitude,
    #     'longitude', body.position.longitude,
    #     'speed', body.position.speed,
    #     'course', body.position.course,
    #     'totalDistance', body.position.attributes.totalDistance,
    #     'lastUpdate', body.device.lastUpdate,
    #     'ignition', ignition,
    #     'alarm', alarm,
    #     'pushedtoServer', false,
    #     'geofenceIds', JSON.stringify(body.device.geofenceIds),
    #     'posAttr', JSON.stringify(body.position.attributes));
    # // console.log(`Data set in redis by micoroservice push_position_redis for ${redisKey}`);
    # // res.end(`Data set in redis by micoroservice push_position_redis for ${redisKey}`);
    # res.end();

    # body.device
    # {"position": {"id": 3144159190,
    #               "attributes": {"sat": 12, "ignition": true, "door": false, "event": 0, "archive": false,
    #                              "distance": 69.99, "totalDistance": 8554243.28, "motion": true, "hours": 6038728000,
    #                              "batteryLevel": 66}, "deviceId": 13460, "type": null, "protocol": "lt05",
    #               "serverTime": "2020-05-06T10:03:51.718+0000", "deviceTime": "2020-05-06T10:03:50.000+0000",
    #               "fixTime": "2020-05-06T10:03:50.000+0000", "outdated": false, "valid": true,
    #               "latitude": 26.144580555555553, "longitude": 85.91469500000001, "altitude": 0,
    #               "speed": 8.099355000000001, "course": 86, "address": null, "accuracy": 0,
    #               "network": {"radioType": "gsm", "considerIp": false, "cellTowers": [
    #                   {"cellId": 52401, "locationAreaCode": 5712, "mobileCountryCode": 405, "mobileNetworkCode": 70}]}},
    #  "device": {"id": 13460,
    #             "attributes": {"alertNumber": "", "countryCode": "", "centerNumber": "", "prevOdometer": 8463290.99,
    #                            "overspeedAlert": "1", "overspeedValue": "101", "vibrationAlert": "0"}, "groupId": 0,
    #             "name": "Dr.H.S PARSAD", "uniqueId": "861910228024078", "status": "online",
    #             "lastUpdate": "2020-05-06T10:03:51.718+0000", "positionId": 3144157314, "geofenceIds": [1123],
    #             "phone": "5755020024135", "model": "LT05+", "contact": null, "category": "car", "disabled": false}}