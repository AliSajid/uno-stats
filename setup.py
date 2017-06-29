"""
Setup.py file for the uno-stats project.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Uno Statistics Calculator',
    'author': 'Ali Sajid Imami',
    'url': 'TBD',
    'download_url': 'TBD',
    'author_email': 'Ali.Sajid.Imami@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'coverage'],
    'packages': ['uno-stats'],
    'scripts': [],
    'name': 'uno-stats'
}

setup(**config)