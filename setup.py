# setup.py

from setuptools import setup, find_packages

setup(
    name='random_quote_cli',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'random-quote-cli = random_quote.cli:main',
        ],
    },
)
