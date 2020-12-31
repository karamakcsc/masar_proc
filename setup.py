# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in masar_proc/__init__.py
from masar_proc import __version__ as version

setup(
	name='masar_proc',
	version=version,
	description='Managing Procurement Procedures',
	author='KCSC',
	author_email='yghoul@kcsc.com.jo',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
