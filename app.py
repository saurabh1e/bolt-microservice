from celery import Celery
from flask import Flask, request
from flask_redis import FlaskRedis
from flask_socketio import SocketIO
from utils.sms import sms
from utils.fcm_notification import fcm_notification
from utils.short_url import dynamic_link

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['MSG91_KEY'] = 'ddddddd'
app.config['MSG91_URL'] = 'http://api.msg91.com/api/v2/sendsms'
app.config['MAIL_DEFAULT_SENDER'] = 'no-reply@test.com'
app.config['MAIL_SENDGRID_API_KEY'] = ''

app.config['TESTING'] = True
app.config['DEBUG'] = False
app.config['REDIS_URL'] = "redis://:@localhost:6379/0"
app.config['CELERY_BROKER_URL'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user:password@host/db'

socketio = SocketIO(app)
celery = Celery(app.name, broker='amqp://:@localhost:5672/')
redis = FlaskRedis(app)
sms.init_app(app)
dynamic_link.init_app(app)


@app.route('/')
def index():
    return '200'


@app.route('/save_position', methods=['POST'])
def save_position():
    celery.send_task('save_position', [request.json])
    return '200'


@app.route('/send_sms')
def send_sms():
    return '200'


if __name__ == '__main__':
    socketio.run(app)