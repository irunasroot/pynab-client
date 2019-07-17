"""
setup.py
Author: Dennis Whitney
Email: dennis@runasroot.com
Copyright (c) 2019, iRunAsRoot
"""

from distutils.core import setup
setup(
  name="pynab-client",
  packages=["pynabapi"],
  version="0.1",
  license="GNU GPLv3",
  description="Python API to access YNAB v1 API",
  author="Dennis Whitney",
  author_email="dennis@irunasroot.com",
  url="https://github.com/irunasroot/pynab-client",
  download_url="https://github.com/irunasroot/pynab-client/archive/v0.1.tar.gz",
  keywords=["ynab", "pynab", "budgeting", "budgets"],
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
