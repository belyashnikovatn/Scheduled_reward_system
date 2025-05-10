#!/bin/bash

# entrypoint.sh

echo "Waiting for PostgreSQL..."
python << END
import socket
import time
import os

host = os.getenv('DB_HOST', 'db')
port = 5432

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        break
    except socket.error:
        time.sleep(1)
END
echo "PostgreSQL started"

if [ "$ROLE" = "web" ]; then
  python manage.py migrate
  python manage.py create_initial_users
fi

exec "$@"