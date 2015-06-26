#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2008-2015 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/dill/LICENSE

from __future__ import with_statement, absolute_import

from os import path
from setuptools import setup, find_packages
from distutils.file_util import copy_file
import sys

_here = path.abspath(path.dirname(__file__))

copy_file(path.join(_here, 'README.rst'), path.join(_here, 'dill'))
copy_file(path.join(_here, 'LICENSE'), path.join(_here, 'dill'))

with open(path.join(_here, 'README.rst')) as f:
    long_description = f.read()

install_requires = []
if sys.platform == "win32":
    install_requires.append('pyreadline>=1.7.1')
    
# build the 'setup' call
setup(
    name='dill',
    use_scm_version={
        'version_scheme': 'guess-next-dev',
        'local_scheme': 'dirty-tag',
        'write_to': 'dill/_version.py'
    },
    setup_requires=['setuptools-scm>=1.5.2,!=1.5.3,!=1.5.4'],
    description='a utility for serialization of python objects',
    long_description = long_description,
    author = 'Mike McKerns',
    maintainer = 'Mike McKerns',
    maintainer_email = 'mmckerns@caltech.edu',
    license = 'BSD',
    platforms = ['any'],
    url = 'http://www.cacr.caltech.edu/~mmckerns',
    classifiers = ('Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Physics Programming'),

    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['LICENSE', '*.rst']},
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'optional': ['objgraph>=1.7.2', 'numpy>=1.6'],
    },
    entry_points={
        'console_scripts': [
            'get_objgraph = dill.get_objgraph:main',
            'unpickle = dill.unpickle:main',
        ],
    },
)
