'''run.py'''

import redis

from flask import Flask, request, jsonify


app = Flask(__name__)
client = redis.StrictRedis(host='redis')


@app.route('/schedule', methods=['POST'])
def schedule():
    '''Push start_urls from POST data to Redis.'''
    data = request.get_json()
    key = '{}:start_urls'.format(data.get('spider'))
    client.lpush(key, data.get('start_urls'))
    return jsonify({'status': 'success'})
