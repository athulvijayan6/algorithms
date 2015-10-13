#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2015-10-12 18:13:23
# @Last Modified by:   athul
# @Last Modified time: 2015-10-13 08:22:55
import random

class node(object):
    """Node of the tree"""
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        

class bst:
    """Implements a binary search tree which supports insertion, deletion, queries,
    range queries. Tree can be created with or without randomization. Randomization is recommended as it will give an expected height of log(n)
    """
    def isempty(self):
        return self.root == None

    def inorderTreeWalk(self, seq, x):
        while x not None:
            seq = inorderTreeWalk(seq, x.left)
            seq.append(x)
            seq = inorderTreeWalk(seq, x.right)
        return seq

    def inorderTreeWalk(self):
        x = self.root
        seq = []
        seq = inorderTreeWalk(seq=seq)
        return seq

    def insert(self, keys):
        for key in keys:
            newNode = node(key)
            y = None
            x = self.root
            while x:
                y = x
                if newNode.key < x.key:
                    x = x.left                
                else:
                    x = x.right
            newNode.parent = y

            if y == None:
                self.root = newNode
            elif newNode.key < y.key:
                y.left = newNode
            else:
                y.right = newNode

    def _exchange(self, x, z):
        z.right = u.right
        z.left = u.left
        if u.parent == None:
            self.root = z
        elif u == u.parent.left:
            u.parent.left = z
        else:
            u.parent.right = z



    def delete(self, x):
        if x.left == None:
            self._exchange(x, x.right)
        elif x.right == None:
            self._exchange(x, x.left)
        else:
            y = self.min(x.right)
            if y.parent != x:
                self._exchange(y, y.right)
                y.right = x.right
                y.right.parent = y
            self._exchange(x, y)
            y.left = z.left
            y.left.parent = y

    def search(self, x, key):
        if x == None or key == x.key:
            return x
        if key < x.key:
            self.search(x.left, key)
        else:
            self.search(x.right, key)

    def search(self, key):
        x = self.root
        return self.search(self, x, key)

    def min(self, x):
        while x.left != None:
            x = x.left
        return x

    def min(self):
        x = self.root
        return self.min(x)

    def max(self, x):        
        while x.right != None:
            x = x.right
        return x

    def max(self):
        x = self.root
        return self.max(x)

    def __init__(self, keys=[], randomize=True):
        self.tree = []
        self.root = None
        if keys:
            # make a bst from the input list of items. When you want to make a bst using other objects, pass in the keys to this function
            if randomize:
                random.shuffle(keys)
            self.insert(keys)

    # def __eq__(self, other):

    # def __ne__(self, other):
