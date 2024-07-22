#!/bin/bash

# Remove old build directories
#rm -rf build dist *.egg-info

# Build the project
#python setup.py sdist bdist_wheel

# Check the dist directory to see the created distribution files
#ls dist

# Upload to pypi
#twine upload dist/*

# build using pyinstaller
pyinstaller --onefile random_quote/cli.py

# verify
pyi-archive_viewer -l dist/cli.exe

# scan
#Use tools like pip-audit, safety, or bandit to regularly audit your dependencies for known vulnerabilities.
#pip install pip-audit safety bandit
pip-audit
#safety check
#bandit -r your_project_directory