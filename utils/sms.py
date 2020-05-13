import requests
from requests.exceptions import Timeout, ConnectionError


class SMS(object):

    key = None
    url = None
    headers = {'content-type': 'application/json'}

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app=None):
        self.key = app.config.get('MSG91_KEY', None)
        self.url = app.config.get('MSG91_URL', None)

    def send_sms(self, sender='RDCAST', route=4, country=91, key=None, content=None):
        print(dict(sender=sender, route=route, country=country, sms=content))
        print(key or self.key)
        try:
            response = requests.post(self.url, json=dict(sender=sender, route=route, country=country, sms=content),
                                     headers={'content-type': 'application/json', 'authkey': key or self.key}, timeout=5)
        except (Timeout, ConnectionError) as e:
            print(e)
            raise e
        return response


sms = SMS()
