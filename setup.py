#!/usr/bin/env python

from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name='django-site-metatags',
    version='0.2',
    author='Eli Dickinson',
    author_email='eli@industrydive.com',
    description='Managing metatags and other SEO in Django, per-site',
    url='http://github.com/industrydive/django-site-metatags',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
