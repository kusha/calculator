#!/usr/bin/env python3

"""
Installation script. Installs mathlib library and rhcalc command.
"""

__author__ = "Mark Birger, Daniil Khudiakov, Martin Knotek"
__date__ = "26 Apr 2015"
__credits__ = ["Mark Birger", "Daniil Khudiakov", "Martin Knotek"]

__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Mark Birger"
__status__ = "Production"

from setuptools import setup
 
setup(
    name='redhead_calculator',
    version='1.0',
    description='Basic calculator with GUI.',
    author='Mark Birger, Daniil Khudiakov, Martin Knotek',
    author_email='xbirge00@stud.fit.vutbr.cz',
    url='https://github.com/kusha/calculator',
    py_modules=['calculator', 'mathlib'],
    entry_points={
        'console_scripts': [
            'rhcalc = calculator:main',
        ],
    })
