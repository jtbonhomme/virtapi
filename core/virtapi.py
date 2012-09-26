"""Basic Libraries"""

import simplejson

""" WebApp """

WEBAPP_ROOT = "/Users/jean-thierrybonhomme/Developments/g7/webapp/public"
WEBAPP_JS_ROOT = "/Users/jean-thierrybonhomme/Developments/g7/webapp/public"
WEBAPP_CSS_ROOT = "/Users/jean-thierrybonhomme/Developments/g7/webapp/public"
DATA_ROOT = "/Users/jean-thierrybonhomme/Developments/virtapi/data"

""" REST API Flask framework """

from flask import Flask, send_from_directory
app = Flask(__name__)

""" Routes for launching the WebApp """

@app.route('/', methods=['GET'])
def get_index():
	return send_from_directory(WEBAPP_ROOT, "index.html")

@app.route('/index.html', methods=['GET'])
def get_index_html():
	return send_from_directory("/Users/jean-thierrybonhomme/Developments/g7/webapp/public", "index.html")

@app.route('/js/g7-webapp.js', methods=['GET'])
def get_js():
	return send_from_directory('/Users/jean-thierrybonhomme/Developments/g7/webapp/public/js', 'g7-webapp.js')

@app.route('/css/g7-webapp.css', methods=['GET'])
def get_css():
	return send_from_directory('/Users/jean-thierrybonhomme/Developments/g7/webapp/public/css', 'g7-webapp.css')

""" Routes for basic calls """

@app.route('/channels', methods=['GET'])
def get_channels():
	return send_from_directory(DATA_ROOT, 'channels.json')

@app.route('/programs/now', methods=['GET'])
def get_now():
	return send_from_directory(DATA_ROOT, 'now.json')

@app.route('/programs/next', methods=['GET'])
def get_next():
	return send_from_directory(DATA_ROOT, 'next.json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)


