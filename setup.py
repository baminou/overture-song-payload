from distutils.core import setup
from setuptools import find_packages

setup(
    name='overture_song_payload',
    version='0.0.4',
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    url="https://github.com/baminou/overture-song-payload",
    install_requires=[
        'jsonschema==2.6.0','setuptools==40.0.0'
    ]
)