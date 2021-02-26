
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="soapsnow",
    version="0.1.3",
    author="Ezequiel M. Iglesias",
    author_email="ezequiel.m.iglesias@gmail.com",
    description="A simple Python library for interacting with ServiceNow's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xthehatterx/soapsnow",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ]
)