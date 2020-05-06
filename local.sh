#!/usr/bin/env bash
export FLASK_APP=covidtracker
export FLASK_ENV=development
pip3 install -e .
python3 webapp/covidtracker/app.py