#!/bin/bash
# Script to deploy our Django instance. Calls Apache mod_wsgi_express to start
# its daemon, and populates a clean database instance with example data.
#
# This script will be called by docker-compose.yml from the parent directory.
APP_BASE=/app
DJANGO_BASE=$APP_BASE/app
WSGI_FILE=$DJANGO_BASE/core/wsgi.py

# No database-level commands are used outside of our API µ-service.

#python $DJANGO_BASE/manage.py flush
python $DJANGO_BASE/manage.py makemigrations
python $DJANGO_BASE/manage.py migrate
#python $DJANGO_BASE/manage.py loaddata $APP_BASE/db.json
mod_wsgi-express start-server --reload-on-changes --deadlock-timeout 10 --graceful-timeout 5 --log-to-terminal --working-directory $DJANGO_BASE $WSGI_FILE
