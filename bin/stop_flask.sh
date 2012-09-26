#!/bin/sh

FLASK_PID_FILE=tmp/restart_flask.pid

if [ -f "$FLASK_PID_FILE" ]; then
	FLASK_PID=`cat $FLASK_PID_FILE`
	echo "Stopping Flask running on pid $FLASK_PID"
	kill $FLASK_PID
	rm $FLASK_PID_FILE
else
	echo "Flask is not running"
fi
exit 0
