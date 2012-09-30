"""Basic Libraries"""

import simplejson
import time

""" WebApp directory (symb. link) """

DATA_ROOT = "/Users/jean-thierrybonhomme/Developments/virtapi/static"

""" REST API Flask framework """

from flask import Flask, send_from_directory
app = Flask(__name__)

""" SSE implementation """

msgList = []

def event_stream():
    for message in msgList:
        """ update message queue length """
        get_message.lastLength=len(msgList)
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
    message = flask.request.form['message']
    user = flask.session.get('user', 'anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()
    """ add message to queue """
    msgList.append('[%s] %s: %s' % (now.isoformat(), user, message))
    return flask.Response('message posted',
                          mimetype="text/html")
@app.route('/stream')
def stream():
    """ check message delivery service """
    return flask.Response(get_message(),
                          mimetype="text/event-stream")

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


