#!/usr/bin/env python

import pathlib

from setuptools import find_packages, setup


VERSION = "0.0.1"

REPO_ROOT = pathlib.Path(__file__).parent

with open(REPO_ROOT / "README.md", encoding="utf-8") as f:
    README = f.read()

REQUIREMENTS = [
    "requests",
]


setup_args = dict(
    # Description
    name="terraform-client",
    version=VERSION,
    description="HashiCorp Terraform Cloud API client",
    long_description=README,
    long_description_content_type="text/markdown",
    # Credentials
    author="Noos Energy",
    author_email="contact@noos.energy",
    url="https://github.com/noosenergy/terraform-client",
    license="MIT",
    # Package data
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["*tests*"]),
    # Dependencies
    platforms=["Any"],
    install_requires=REQUIREMENTS,
)


if __name__ == "__main__":

    # Make install
    setup(**setup_args)
