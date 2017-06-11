import os
import random
import json
import datetime
import hashlib
import base64
import requests

# Adobe API credentials
# Your API Username and Shared Secret can be found under Account Information
# in the Web Service section of Adobe Analytics.
ADOBE_CREDENTIALS = {
    'user_name': os.environ['ADOBE_USERNAME'],
    'secret': os.environ['ADOBE_SECRET']
}
# RSID
REPORT_SUITE = 'production'


def request_to_api(user_name, secret, method, params={}):
    nonce = str(random.getrandbits(128)).encode()
    nonce_ts = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ').encode()
    digest = base64.b64encode(hashlib.sha1(
        nonce + nonce_ts + secret.encode()).hexdigest().encode())
    endpoint = 'https://api.omniture.com/admin/1.4/rest/'
    url = endpoint + '?method=' + method
    headers = {
        'X-WSSE': 'UsernameToken Username="' + user_name + '", PasswordDigest="' +
        digest.decode('utf-8') + '", Nonce="' + nonce.decode('utf-8') + '", Created="' +
        nonce_ts.decode('utf-8') + '"'
    }
    r = requests.post(url, data=json.dumps(params), headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        r.raise_for_status()
