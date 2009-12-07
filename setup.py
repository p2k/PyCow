#!/usr/bin/env python

from distutils.core import setup

setup(
	name='PyCow',
	version='0.3',
	description='Python to JavaScript converter',
	author='p2k',
	author_email='patrick.p2k.schneider@gmail.com',
	url='http://github.com/p2k/PyCow',
	packages=['pycow'],
	package_data={'pycow': ['js/pycow.js', 'demo/*']},
	scripts=['scripts/pycow'],
)

