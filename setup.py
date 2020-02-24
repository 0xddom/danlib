# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="danlib",
    author="Daniel Domínguez",
    author_email="daniel.dominguez@imdea.org",
    url="https://github.com/0xddom/danlib",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    license="WTFPL",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    description="Module for stuff useful to me that doesn't deserve its own module."
)
