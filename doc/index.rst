.. pytemplate documentation master file, created by
   sphinx-quickstart on Tue Oct 21 10:21:50 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

documentation for pytemplate's
==============================

.. image:: https://travis-ci.org/phobson/pytemplate.svg?branch=master
    :target: https://travis-ci.org/phobson/pytemplate
    :alt: Build Status

.. image:: https://coveralls.io/repos/phobson/pytemplate/badge.png?branch=master
    :target: https://coveralls.io/r/phobson/pytemplate?branch=master
    :alt: Test Coverage

.. image:: https://readthedocs.org/projects/pytemplate/badge/?version=latest
    :target: https://readthedocs.org/projects/pytemplate/?badge=latest
    :alt: Documentation Status

``pytemplate`` is an example python library meant to demostrate how to:
 * use  ``nose`` to write unit tests
 * use numpy, pandas, and matplotlib speciality testing functions
 * use Travis CI to run unit tests
 * use Coveralls.io to examine and report test coverage
 * use restructured text, ``sphinx``, andreadthedocs.org to document your code.

Dependencies
------------
.. TODO: list dependencies

Installation
------------

* Activate your ``conda`` environment;
* Clone my fork from Github;
* Change to that resulting directory;
* Install via pip; and
* Back out of that directory to use

::

    source activate metar # (omit "source" on Windows)
    git clone https://github.com/phobson/pytemplate
    cd pytemplate
    pip install .
    cd ../..

Testing
-------

Tests are run via ``nose``. Run them all with: ::

    source activate pytemplate # (omit "source" on Windows)
    python -c "import pytemplate; pytemplate.test()"

You can get fancy with: ::

    python -c "import pytemplate; pytemplate.test(verbose=2, packageinfo=True, coverage=True)"

Contents:
---------

.. toctree::
   :maxdepth: 2

   Events <core/events>
   Features <core/features>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

