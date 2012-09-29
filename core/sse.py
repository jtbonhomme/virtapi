#!/usr/bin/env python
import datetime
import flask

app = flask.Flask(__name__)
""" shall create a secret_key in order to use flask sessions """
app.secret_key = 'asdf'

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        flask.session['user'] = flask.request.form['user']
        """ new user logged registered """
        return flask.redirect('/')
    return '<form action="" method="post">user: <input name="user">'

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

@app.route('/')
def home():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    return """
        <!doctype html>
        <title>chat</title>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <style>body { max-width: 500px; margin: auto; padding: 1em; background: black; color: #fff; font: 16px/1.6 menlo, monospace; }</style>
        <p><b>hi, %s!</b></p>
        <p>Message: <input id="in" /></p>
        <pre id="out"></pre>
        <script>
            function sse() {
                var source = new EventSource('/stream');
                var out = document.getElementById('out');
                source.onmessage = function(e) {
                    // XSS in chat is fun
                    if( e.data != "" )
                        out.innerHTML =  e.data + '\\n' + out.innerHTML;
                };
            }
            $('#in').keyup(function(e){
                if (e.keyCode == 13) {
                    $.post('/post', {'message': $(this).val()});
                    $(this).val('');
                }
            });
            sse();
        </script>

    """ % flask.session['user']

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=1234)

