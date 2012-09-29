virtapi
=======

Virtual REST API based on FLASK.

<pre>
npm install
ln -s /path/to/statc/file/directory/to/serve static
python core/virtapi.py
</pre>

Note: tested on MAC OS 10.6.8

sse
===

Server-Sent events example in a simple chat application.

This script is inspired from jkbr's chat (https://github.com/jkbr/chat)
It has been modified in order to avoid redis for message queue.

The server-sent events are used to send notification to the client (browser) and the server is based on Flask.

<pre>
npm install
python core/sse.py
</pre>

Note: tested on MAC OS 10.6.8
