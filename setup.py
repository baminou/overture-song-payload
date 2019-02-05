from distutils.core import setup
from setuptools import find_packages

setup(
    name='overture_song_payload',
    version='0.0.3',
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    url=None,
    install_requires=[
        'jsonschema'
    ]
)