#!/bin/sh

FLASK_PID_FILE=tmp/restart_flask.pid


if [ -f "$FLASK_PID_FILE" ]; then
	FLASK_PID=`cat $FLASK_PID_FILE`
	echo "Stopping Flask running on pid $FLASK_PID"
	kill $FLASK_PID
fi

echo "Starting Flask"
python core/virtapi.py &
FLASK_PID=$!
echo $FLASK_PID > $FLASK_PID_FILE
echo "Flask is running on pid $FLASK_PID"

exit 0
