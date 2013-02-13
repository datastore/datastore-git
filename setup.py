#!/usr/bin/env python

import re
from setuptools import setup, find_packages

pkgname = 'datastore.git'

# gather the package information
main_py = open('datastore/git/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", main_py))
packages = filter(lambda p: p.startswith(pkgname), find_packages())

# convert the readme to pypi compatible rst
try:
  try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
  except ImportError:
    readme = open('README.md').read()
except:
  print 'something went wrong reading the README.md file.'
  readme = ''

setup(
  name=pkgname,
  version=metadata['version'],
  description='git datastore implementation',
  long_description=readme,
  author=metadata['author'],
  author_email=metadata['email'],
  url='http://github.com/datastore/datastore.git',
  keywords=[
    'datastore',
    'git',
    'dulwich',
  ],
  packages=packages,
  install_requires=['datastore>=0.3.0', 'dulwich>=0.8.7'],
  test_suite='datastore.git.test',
  license='MIT License',
  classifiers=[
    'Topic :: Database',
    'Topic :: Database :: Front-Ends',
    'Topic :: Datastore :: Implementation',
  ]
)
