#!/bin/bash

#PATHS FOR PYSPARK TO WORK AND OTHER PYTHON LIBRARIES. TAKEN FROM BASH PROFILE.
export SPARK_HOME=""
export PATH=$PATH:$SPARK_HOME/bin
export PYSPARK_PYTHON=python3
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip:$PYTHONPATH
export SPARK_LOCAL_IP=localhost
PATH="/path/to/Python.framework/:${PATH}"
export PATH
alias python='python3' 

#PATH TO SCRIPT
python /path/to/script.py


