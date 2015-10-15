#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2015-10-12 18:13:23
# @Last Modified by:   Athul
# @Last Modified time: 2015-10-15 17:26:29

class node(object):
    """Node of the tree"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = None
        self.left = None
        self.right = None
        self.parent = None        

class bst:
    """Implements a binary search tree (not balanced) which supports insertion, deletion, queries. Tree can be created with or without randomization. Randomization is recommended as it will give an expected height of log(n)
    """
    def isempty(self):
        # Checks if tree is empty
        return self.root == None

    def _inorderTreeWalk(self, seq, x):
        # Walks through the subtree with root x in increasing order of key values
        # O(n) complexity 
        if x != None:
            seq = self._inorderTreeWalk(seq, x.left)
            seq.append(x)
            seq = self._inorderTreeWalk(seq, x.right)
        return seq

    def inorderTreeWalk(self, x=None):
        # Walks through the whole tree in increasing order of key values.
        # O(n) complexity
        if x == None:
            x = self.root
        seq = []
        seq = self._inorderTreeWalk(seq=seq, x=x)
        return seq

    def insert(self, keys):
        # insert nodes into the tree pass as a list of key value tuples (key, value)
        # O(logn) complexity
        for key, value in keys:
            newNode = node(key, value)
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

    def _transplant(self, u, z):
        # transplants a node with another subtree
        if u.parent == None:
            self.root = z
        elif u == u.parent.left:
            u.parent.left = z
        else:
            u.parent.right = z
        if z != None:
            z.parent = u.parent


    def delete(self, x):
        # Deletes a particular node given as input
        # Operation takes O(logn) time
        if x.left == None:
            self._transplant(x, x.right)
        elif x.right == None:
            self._transplant(x, x.left)
        else:
            y = self.min(x.right)
            if y.parent != x:
                self._transplant(y, y.right)
                y.right = x.right
                y.right.parent = y
            self._transplant(x, y)
            y.left = x.left
            y.left.parent = y

    def _search(self, x, key):
        # Searches for a node with the given key within a subtree rooted at x
        # Operation takes O(logn) time
        if x == None or key == x.key:
            return x
        if key < x.key:
            self._search(x.left, key)
        else:
            self._search(x.right, key)

    def search(self, key, x=None):
        # Searches for a node with the given key within whole tree
        # Operation takes O(logn) time
        if x == None:
            x = self.root
        return self._search(x, key)

    def _min(self, x):
        # minimum of subtree rooted at x
        # Operation takes O(logn) time
        while x.left != None:
            x = x.left
        return x

    def min(self, x=None):
        # minimum of whole tree
        # Operation takes O(logn) time
        if x == None:
            x = self.root
        return self._min(x)

    def _max(self, x):
        # maximum of subtree rooted at x
        # Operation takes O(logn) time       
        while x.right != None:
            x = x.right
        return x

    def max(self, x=None):
        # maximum of whole tree
        # Operation takes O(logn) time
        if x == None:
            x = self.root
        return self._max(x)

    def __init__(self, keys=[], randomize=True):
        self.root = None
        if keys:
            # make a bst from the input list of items.
            if randomize:
                import random
                random.shuffle(keys)
            self.insert(keys)


class AVLnode(object):
    """Node of the tree"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = None
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __repr__(self):
        return str(self.key)

def _height(x):
    if x != None:
        return x.height
    else:
        return -1

class AVLtree:
    """Implements a balanced binary search tree (AVL tree) which supports insertion, deletion, queries,
    """
    def isempty(self):
        # Checks if tree is empty
        return self.root == None

    def _inorderTreeWalk(self, seq, x):
        # Walks through the subtree with root x in increasing order of key values
        # O(n) complexity 
        if x != None:
            seq = self._inorderTreeWalk(seq, x.left)
            seq.append(x)
            seq = self._inorderTreeWalk(seq, x.right)
        return seq

    def inorderTreeWalk(self, x=None):
        # Walks through the whole tree in increasing order of key values.
        # O(n) complexity
        if x == None:
            x = self.root
        seq = []
        seq = self._inorderTreeWalk(seq=seq, x=x)
        return seq

    def _rotateLeft(self, x):
        k2 = x.left

        x.left = k2.right
        if x.right != None:
            x.right.parent = x
        
        k2.parent = x.parent
        if x.parent != None:
            if x == x.parent.left:
                x.parent.left = k2
            else:
                x.parent.right = k2

        x.parent = k2
        k2.right = x

        if self.root == x:
            self.root = k2

        x.height = max(_height(x.right), _height(x.left)) + 1
        k2.height = max(_height(k2.right), _height(k2.left)) + 1

    def _rotateRight(self, x):
        k2 = x.right

        x.right = k2.left
        if x.right != None:
            x.right.parent = x
        
        k2.parent = x.parent
        if x.parent != None:
            if x == x.parent.left:
                x.parent.left = k2
            else:
                x.parent.right = k2

        x.parent = k2
        k2.left = x

        if self.root == x:
            self.root = k2

        x.height = max(_height(x.right), _height(x.left)) + 1
        k2.height = max(_height(k2.right), _height(k2.left)) + 1

    def _doubleRotateLeft(self, k3):
        self._rotateRight(k3.left)
        self._rotateLeft(k3)

    def _doubleRotateRight(self, k3):
        self._rotateLeft(k3.right)
        self._rotateRight(k3)

    def _balance(self, x):
        if x == None:
            return False
        if _height(x.left) - _height(x.right) > 1:
            # balance left subtree
            if _height(x.left.left) >= _height(x.left.right):
                # single rotate left
                self._rotateLeft(x)
            else:
                # double rotate left
                self._doubleRotateLeft(x)

        elif  _height(x.right) - _height(x.left) > 1:
            # balance right subtree
            if _height(x.right.right) >= _height(x.right.left):
                # single rotate right
                self._rotateRight(x)
            else:
                # double rotate right
                self._doubleRotateRight(x)

        # Now update the height
        x.height = max(_height(x.right), _height(x.left)) + 1

    def _insert(self, u, y, x):
        if y == None:
            self.root = u
        elif x == None:
            if u.key < y.key:
                y.left = u
            elif (u.key > y.key):
                y.right = u
            u.parent = y
        elif u.key < x.key:
            self._insert(u, x, x.left)
        elif u.key >= x.key:
            self._insert(u, x, x.right)
        self._balance(x)     

    def insert(self, keys):
        # insert nodes into the tree pass as a list of key value tuples (key, value)
        # O(logn) complexity
        for key, value in keys:
            newNode = AVLnode(key, value)
            self._insert(newNode, self.root, self.root)

    def _transplant(self, u, z):
        # transplants a node with another subtree
        if u.parent == None:
            self.root = z
        elif u == u.parent.left:
            u.parent.left = z
        else:
            u.parent.right = z
        if z != None:
            z.parent = u.parent

    def _delete(self, u, x):
        # Deletes a particular node given as input
        # Operation takes O(logn) time
        if x == None:
            return False
        elif u.key < x.key:
            self._delete(u, x.left)
        elif u.key > x.key:
            self._delete(u, x.right)
        # matched node, two children exist
        elif (x.left != None) and (x.right != None):
            y = self.min(x.right)
            if y.parent != x:
                self._transplant(y, y.right)
                y.right = x.right
                y.right.parent = y
            self._transplant(x, y)
            y.left = x.left
            y.left.parent = y
        # matched node, only one children exist
        else:
            if x.left == None:
                self._transplant(x, x.right)
            elif x.right == None:
                self._transplant(x, x.left)

        self._balance(x)


    def delete(self, u):
        self._delete(u, self.root)


    def _search(self, x, key):
        # Searches for a node with the given key within a subtree rooted at x
        # Operation takes O(logn) time
        if x == None or key == x.key:
            return x
        if key < x.key:
            self._search(x.left, key)
        else:
            self._search(x.right, key)

    def search(self, key, x=None):
        # Searches for a node with the given key within whole tree
        # Operation takes O(logn) time
        if x == None:
            x = self.root
        return self._search(x, key)

    def _min(self, x):
        # minimum of subtree rooted at x
        # Operation takes O(logn) time
        while x.left != None:
            x = x.left
        return x

    def min(self, x=None):
        # minimum of whole tree
        # Operation takes O(logn) time
        if x == None:
            x = self.root
        return self._min(x)

    def _max(self, x):
        # maximum of subtree rooted at x
        # Operation takes O(logn) time       
        while x.right != None:
            x = x.right
        return x

    def max(self, x=None):
        # maximum of whole tree
        # Operation takes O(logn) time
        if x == None:
            x = self.root
        return self._max(x)

    def __init__(self, keys=[]):
        self.root = None
        if keys:
            # make a AVL tree from the input list of items.
            self.insert(keys)