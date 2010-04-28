#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: test binary trees
# Created: 28.04.2010

import sys
import unittest2 as unittest
from random import randint

from bintrees.bintree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    default_values1 = zip([12, 34, 45, 16, 35, 57], [12, 34, 45, 16, 35, 57])
    default_values2 = [(2, 12), (4, 34), (8, 45), (1, 16), (9, 35), (3, 57)]
    def test_create_tree(self):
        tree = BinaryTree()
        self.assertEqual(len(tree), 0)
        tree.update(self.default_values1)
        self.assertEqual(len(tree), 6)

    def test_iter_tree(self):
        tree = BinaryTree(self.default_values1)
        result = list(iter(tree))
        self.assertEqual(result, [12, 16, 34, 35, 45, 57])

    def test_get_items(self):
        tree = BinaryTree(self.default_values1)
        self.assertEqual(tree.get(34), 34)
        self.assertEqual(tree.get(12), 12)

    def test_remove_inner_node(self):
        tree = BinaryTree(self.default_values1)
        tree.remove(34)
        node = tree._find_node(tree.root, 35)
        self.assertEqual(node.left.value, 16)
        self.assertEqual(node.right.value, 45)
        self.assertEqual(len(tree), 5)

    def test_remove_root(self):
        tree = BinaryTree(self.default_values1)
        tree.remove(12)
        self.assertEqual(tree.root.value, 34)
        self.assertEqual(tree.root.parent, None)
        self.assertEqual(len(tree), 5)

    def test_remove_leaf_node(self):
        tree = BinaryTree(self.default_values1)
        tree.remove(57)
        node = tree._find_node(tree.root, 45)
        self.assertEqual(node.left.value, 35)
        self.assertEqual(node.right, None)
        self.assertEqual(len(tree), 5)

    def test_delete_node(self):
        tree = BinaryTree(self.default_values1)
        del tree[57]
        node = tree._find_node(tree.root, 45)
        self.assertEqual(node.left.value, 35)
        self.assertEqual(node.right, None)
        self.assertEqual(len(tree), 5)

    def test_random_numbers(self):
        tree = BinaryTree()
        for x in xrange(1000):
            val = randint(0, 10000)
            tree[val] = val
        self.assertGreater(len(tree), 0)
        generator = iter(tree)
        a = generator.next()
        for b in generator:
            self.assertGreaterEqual(b, a)
        count = tree._count
        tree.count() # recount
        self.assertEqual(count, len(tree))

    def test_index_operator(self):
        tree = BinaryTree(self.default_values1)
        self.assertEqual(tree[45], 45)
        tree[99] = 99

    def test_complex_data(self):
        tree = BinaryTree(self.default_values2)
        self.assertEqual(tree[8], 45)

    def test_default_vaule(self):
        tree = BinaryTree(self.default_values2)
        self.assertEqual(tree.get(7, "DEFAULT"), "DEFAULT")

    def test_has_key(self):
        tree = BinaryTree(self.default_values2)
        self.assertTrue(tree.has_key(8))
        self.assertFalse(tree.has_key(11))
        self.assertTrue( 8 in tree)
        self.assertFalse(8 not in tree)
        self.assertFalse(11 in tree)
        self.assertTrue(11 not in tree)

    def test_pop(self):
        tree = BinaryTree(self.default_values2)
        data = tree.pop(8)
        self.assertEqual(data, 45)
        self.assertFalse(8 in tree)
        self.assertRaises(KeyError, tree.pop, 8)
        self.assertEqual(tree.pop(8, 99), 99)

    def test_popitem(self):
        tree = BinaryTree(self.default_values2)
        d = dict()
        while not tree.is_empty():
            key, value = tree.popitem()
            d[key]=value
        expected = {2: 12, 4: 34, 8: 45, 1: 16, 9: 35, 3: 57}
        self.assertEqual(expected, d)
        self.assertRaises(KeyError, tree.popitem)

    def test_iterkeys(self):
        tree = BinaryTree(self.default_values2)
        keys = tree.keys()
        expected = [1, 2, 3, 4, 8, 9]
        self.assertEqual(expected, keys)

    def test_itervalues(self):
        tree = BinaryTree(self.default_values2)
        values = tree.values()
        expected = [16, 12, 57, 34, 45, 35]
        self.assertEqual(expected, values)

    def test_copy(self):
        tree = BinaryTree(self.default_values2)
        copytree = tree.copy()
        self.assertEqual(tree.items(), copytree.items())

    def test_to_dict(self):
        tree = BinaryTree(self.default_values2)
        d = dict(tree)
        self.assertEqual(d, dict(self.default_values2))

    def test_clear(self):
        tree = BinaryTree(self.default_values2)
        tree.clear()
        self.assertEqual(tree.root, None)

    def test_setdefault(self):
        tree = BinaryTree(self.default_values2)
        value = tree.setdefault(2, 17) # key <2> exists and == 12
        self.assertEqual(value, 12)
        value = tree.setdefault(99, 77)
        self.assertEqual(value, 77)
if __name__=='__main__':
    unittest.main()