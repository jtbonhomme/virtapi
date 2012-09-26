#!/bin/sh

FLASK_PID_FILE=tmp/restart_flask.pid

if [ -f "$FLASK_PID_FILE" ]; then
	echo "Flask is running, please stop it or restart it"
	exit 1
fi

echo "Starting Flask"
python core/virtapi.py &
FLASK_PID=$!
echo $FLASK_PID > $FLASK_PID_FILE
echo "Flask is running on pid $FLASK_PID"

exit 0
