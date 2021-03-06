"""Basic Libraries"""

import simplejson
import time

""" WebApp directory (symb. link) """

DATA_ROOT = "/Users/jean-thierrybonhomme/Developments/virtapi/static"

""" REST API Flask framework """

import flask
app = flask.Flask(__name__)
"""from flask import Flask, send_from_directory
app = Flask(__name__)"""

""" SSE implementation """

msgList = []

def event_stream():
    for message in msgList:
        """ update message queue length """
        get_message.lastLength=len(msgList)
        """ CAUTION: SSE requires message to be sent with format data MESSAGE\n\n """
        yield 'data: %s\n\n' % message

eventStream=event_stream()

def get_message():
    if not hasattr(get_message, "lastLength"):
        get_message.lastLength = 0
    if len(msgList) == get_message.lastLength:
        """ no message pending (message queue length did not increased), return """
        return ''
    else:
        """ seems a message has been posted, deliver it """
        return eventStream.next();

@app.route('/post', methods=['POST'])
def post():
    if flask.request.headers['Content-Type'] == 'application/json':
        """ add message to queue """
        msgList.append('%s' % flask.json.dumps(flask.request.json))
    return flask.Response('VIRTUAL: message posted',
                          mimetype="text/html")

""" Route to allow testapp to receive messages """
@app.route('/stream')
def stream():
    """ check message delivery service (get_message) and send response (empty if no message) """
    """ CAUTION: EventSource require mimetype to be event-stream """
    return flask.Response(get_message(),
                          mimetype="text/event-stream")

""" Routes for serving the TestApp """

@app.route('/', methods=['GET'])
def get_default():
    return flask.send_from_directory(DATA_ROOT, 'index_testapp.html')

@app.route('/index_testapp.html', methods=['GET'])
def get_index():
    return flask.send_from_directory(DATA_ROOT, 'index_testapp.html')

@app.route('/style.css', methods=['GET'])
def get_css():
    return flask.send_from_directory(DATA_ROOT, 'style.css')

@app.route('/ajax.js', methods=['GET'])
def get_ajax():
    return flask.send_from_directory(DATA_ROOT, 'ajax.js')

@app.route('/longpoll.js', methods=['GET'])
def get_poll():
    return flask.send_from_directory(DATA_ROOT, 'longpoll.js')

@app.route('/sse.js', methods=['GET'])
def get_sse():
    return flask.send_from_directory(DATA_ROOT, 'sse.js')

@app.route('/app_spec.js', methods=['GET'])
def get_app():
    return flask.send_from_directory(DATA_ROOT, 'app_spec.js')

@app.route('/CanalLightRomain.otf', methods=['GET'])
def get_font():
    return flask.send_from_directory(DATA_ROOT, 'CanalLightRomain.otf')

@app.route('/jquery-1.8.2.min.js', methods=['GET'])
def get_jquery():
    return flask.send_from_directory(DATA_ROOT, 'jquery-1.8.2.min.js')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234)


