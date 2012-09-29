"""Basic Libraries"""

import simplejson
import time

""" WebApp directory (symb. link) """

DATA_ROOT = "/Users/jean-thierrybonhomme/Developments/virtapi/static"

""" REST API Flask framework """

from flask import Flask, send_from_directory
app = Flask(__name__)

""" Routes for communnication with the TestApp """

@app.route('/event', methods=['GET'])
def get_event():
    print "get_event"
    time.sleep(10)
    print "wake-up !"
    return '{"type": "event","params":{"event": "playbackStopped"}}'
"""    return send_from_directory(DATA_ROOT, 'event.json', mimetype='application/json') """

"""
@app.route('/order/<param>', methods=['POST'])
def get_order():
    return ''
"""

""" Routes for serving the TestApp """

@app.route('/index_testapp.html', methods=['GET'])
def get_html():
    return send_from_directory(DATA_ROOT, 'index_testapp.html')

@app.route('/style.css', methods=['GET'])
def get_css():
    return send_from_directory(DATA_ROOT, 'style.css')

@app.route('/ajax.js', methods=['GET'])
def get_ajax():
    return send_from_directory(DATA_ROOT, 'ajax.js')

@app.route('/longpoll.js', methods=['GET'])
def get_poll():
    return send_from_directory(DATA_ROOT, 'longpoll.js')

@app.route('/app_spec.js', methods=['GET'])
def get_app():
    return send_from_directory(DATA_ROOT, 'app_spec.js')

@app.route('/CanalLightRomain.otf', methods=['GET'])
def get_font():
    return send_from_directory(DATA_ROOT, 'CanalLightRomain.otf')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234)


