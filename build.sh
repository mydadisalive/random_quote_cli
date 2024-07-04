#!/bin/bash

# Remove old build directories
rm -rf build dist *.egg-info

# Build the project
python setup.py sdist bdist_wheel

