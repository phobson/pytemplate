# Setup script for the pytemplate package
#
# Usage: python setup.py install
#
import os
from setuptools import setup, find_packages

DESCRIPTION = "pytemplate: A simple one-liner to describe your project"

LONG_DESCRIPTION = """
This should be a long, multi-line description of the project.

You can talk about your motivation and whatnot.
"""

datadir = os.path.join('.', 'data')

setup(
    name="pytemplate",
    version="0.1",
    author="Paul Hobson (Geosyntec Consultants)",
    author_email="phobson@geosyntec.com",
    url="https://github.com/phobson/pytemplate",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    download_url="https://github.com/phobson/pytemplate/archive/master.zip",
    license="BSD 3-clause",
    packages=find_packages(exclude=['cvc']),
    data_files=[
        ('pytemplate_data/bmp/data', [
            d for d in
                map(lambda x: os.path.join(datadir, x), os.listdir(datadir))
            ]
        ),
    ],
    platforms="Python 2.7 and 3.3.",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Topic :: Formats and Protocols :: Data Formats",
        "Topic :: Scientific/Engineering :: Earth Sciences",
        "Topic :: Software Development :: Libraries :: Python Modules"
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        ],
    #install_requires=['seaborn', 'coverage']
)
