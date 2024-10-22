#!/usr/bin/env python

"""setup.py: distutils/setuptools install script."""

from setuptools import setup

REQUIRES = []

try:
    with open("README.md", encoding="utf-8") as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = ""

setup(
    name="amazon-api-gateway-secure-authorizer",
    version="0.1.0",
    author="Efficient Solutions LLC",
    author_email="contact@efficient.solutions",
    description="Secure Lambda authorizer for HTTP API behind CloudFront",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/efficient-solutions/amazon-api-gateway-secure-authorizer",
    packages=["secure_authorizer"],
    license="MIT",
    install_requires=REQUIRES,
    python_requires=">= 3.10",
    keywords=[
        "Amazon API Gateway", "Amazon CloudFront", "AWS Lambda", "AWS Secrets Manager"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ]
)