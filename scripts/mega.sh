#!/bin/bash

source /opt/rcc_api_test/venv/bin/activate && cd /opt/rcc_api_test
python runsuite.py --suites mega --env dev -o "rp_launch_tags=mega" --reportportal