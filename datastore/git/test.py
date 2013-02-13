
import os
import shutil
import unittest

from datastore.core import serialize
from datastore.filesystem.test import TestDatastore
from . import GitDatastore


class TestGitDatastore(TestDatastore):

  tmp = os.path.normpath('.datastore')

  def setUp(self):
    if os.path.exists(self.tmp):
      shutil.rmtree(self.tmp)

  def tearDown(self):
    pass
    # shutil.rmtree(self.tmp)

  def test_datastore(self):
    p = os.path.join(self.tmp, '1')
    g = GitDatastore(p)
    s = serialize.shim(g, serialize.prettyjson)
    self.subtest_simple([s], numelems=100)


if __name__ == '__main__':
  unittest.main()
