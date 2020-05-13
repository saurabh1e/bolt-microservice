import requests


class FireBaseDynamicLink(object):
    key = None

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app=None):
        if app:
            self.key = app.config.get('FIREBASE_DYNAMIC_KEY', None)

    def get_short_link(self, link):
        data = dict(dynamicLinkInfo=dict(domainUriPrefix='https://jeebly-tracking.web.app/', link=link), suffix={"option": "SHORT"})
        res = requests.post('https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=' + self.key, json=data)

        if res.status_code == 200:
            return res.json()['shortLink']
        return None


dynamic_link = FireBaseDynamicLink()
