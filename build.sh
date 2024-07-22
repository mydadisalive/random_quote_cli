#!/bin/bash

# Remove old build directories
rm -rf build dist *.egg-info

# Build the project
python setup.py sdist bdist_wheel

# Check the dist directory to see the created distribution files
#ls dist

# Upload to pypi
#twine upload dist/*

# build using pyinstaller
pyinstaller --onefile random_quote/cli.py

# verify
pyi-archive_viewer -l dist/cli.exe