#!/bin/sh

set -e

if [ "${1#-}" != "$1" ]; then
	pip install --no-cache -U -r requirements.txt
	set -- python runsuite.py "$@"
fi

exec "$@"
