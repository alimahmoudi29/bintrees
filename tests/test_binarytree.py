#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: test binary trees
# Created: 28.04.2010

import unittest2 as unittest
from tree_test import TestTreeMixin

from bintrees import BinaryTree

class TestBinaryTree(TestTreeMixin, unittest.TestCase):
    @property
    def TREE(self):
        return BinaryTree

if __name__=='__main__':
    unittest.main()