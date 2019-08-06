"""
setup.py
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

from setuptools import setup

with open("README.md", "r") as md:
  long_description = md.read()


setup(
  name="pynab-client",
  packages=["pynabapi", "pynabapi.model"],
  version="0.2",
  license="GNU GPLv3",
  description="Python API to access YNAB v1 API",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="Dennis Whitney",
  author_email="dennis@irunasroot.com",
  url="https://github.com/irunasroot/pynab-client",
  download_url="https://github.com/irunasroot/pynab-client/archive/v0.2.tar.gz",
  keywords=["ynab", "pynab", "budgeting", "budgets", "youneedabudget"],
  install_requires=[
          "requests"
  ],
  classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3.6",
  ]
)
