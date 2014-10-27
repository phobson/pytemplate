[![Build Status](https://travis-ci.org/phobson/pytemplate.svg?branch=master)](https://travis-ci.org/phobson/pytemplate)
[![Coverage Status](https://coveralls.io/repos/phobson/pytemplate/badge.png)](https://coveralls.io/r/phobson/pytemplate)
[![Documentation Status](https://readthedocs.org/projects/python-template/badge/?version=latest)](https://readthedocs.org/projects/python-template/?badge=latest)

## Motivation
Since I've self-taught myself to program in python, I've picked a number of things
that have been incredibly useful to write good code. However, a handleful of those
things were pretty difficult to get a good, clear, and concise example of how to
make it all work together. Some examples were either too minimal and failed to 
display the nuances and extent of features necessary to get good use out of a tool.
Others were far too detailed and complex. This complicated adapting those examples
for my own use.

So hopefully this template serves and an example for how to get a good scientific
library started up that uses the following features and services:
  1. `nose` (or better yet, `py.test`) for unit testing
  2. Specialized testing function like `numpy.testing`, `pandas.util.testing` and matplotlib's `@image_comparison` decorator
  3. Travis CI for running tests
  4. Coveralls for tracking test coverage
  5. readthedocs.org and restructured text for automated documentation
  6. Creating a `setup.py` file that installs your package, tests, and necessary datasets into the python environment.
  
**This is very much a work-in-progress**

## Setup
Use conda. It's just easier.

### Create your environment
```
conda create --name pytemplate python=3.3 ipython-notebook matplotlib \
                    statsmodels nose pip pyyaml requests coverage \
                    sphinx
```

### clone the repo
```
git clone git@github.com:phobson/pytemplate.git # or use your fork 
```

### move into the report and install
```
cd pytemplate
pip install .
```

### run the tests
```
cd ~
activate pytemplate
python -c "import pytemplate; pytemplate.test(verbose=2, coverage=True"
```
