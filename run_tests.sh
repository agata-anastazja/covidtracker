#!/usr/bin/env bash

#echo $PYTHONPATH
#echo `dirname "$0"`
export DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export PYTHONPATH=$DIR:$PYTHONPATH
echo $PYTHONPATH
python -c 'import covidtracker;print(dir(covidtracker));'
python -c 'import covidtracker;print(dir());'
python -c 'import covidtracker;print(dir(covidtracker/*));'


nosetests --debug=nose,nose.importer --debug-log=nose_debug