from app import celery, redis


@celery.task(name='send_notification')
def send_notification(args):
    print(args)
    print(redis.keys('*'))
