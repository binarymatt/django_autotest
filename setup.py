#!/usr/bin/env python
from setuptools import setup
setup(
    name="django_autotest",
    version="0.1",
    include_package_data=True,
    packages=['django_autotest'],
    install_requires=['django','growl-py'],
    description="Auto tester for django",
    license = "MIT",
    author="Matt George",
    author_email="mgeorge@gmail.com",
    url="http://github.com/binarydud/django_autotest",
)

