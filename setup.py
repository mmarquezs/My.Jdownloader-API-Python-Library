"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="myjdapi",
    version="1.1.9",
    description="Library to use My.Jdownloader API in an easy way.",
    long_description=long_description,
    url="https://github.com/mmarquezs/My.Jdownloader-API-Python-Library/",
    author="Marc Marquez Santamaria",
    author_email="mmsa1994@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="myjdapi jdownloader my.jdownloader api development",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[
        "requests",
        "pycryptodome"
    ],
)
