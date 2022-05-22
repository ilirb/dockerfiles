import os
import sys
import json
import requests
import time
from flask import Flask


TZ = os.getenv("TZ", default="Europe/Stockholm")
os.environ['TZ'] = TZ
APIKEY = os.getenv("APIKEY", default=None)

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

def get_ipify():
    t = time.strftime('%A %B, %d %Y %H:%M:%S')
    try:
        ip = requests.get('https://api.ipify.org').text
        if APIKEY:
            geo = requests.get(f"https://geo.ipify.org/api/v1?apiKey={APIKEY}&ipAddress={ip}")
            data = json.loads(geo.text)
        else:
            data = {
                "ip": ip,
                "geo": "Get your APIKEY from https://geo.ipify.org/ to get Geolocation data and set it as envvar"
            }
        data["time"] = t
        return data
    except Exception as e:
        return e

@app.route('/')
@app.route('/ip')
def ip():
    return get_ipify()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
