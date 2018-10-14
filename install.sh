#!/bin/sh
rm -rf acrosure_sdk.egg-info &&
rm -rf build &&
rm -rf dist &&
python3 setup.py sdist bdist_wheel && pip3 install -e . &&
python2 setup.py sdist bdist_wheel && pip install -e .
