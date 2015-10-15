#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2015-10-12 20:16:22
# @Last Modified by:   Athul
# @Last Modified time: 2015-10-15 17:06:05
import tree.bst as bst
from random import shuffle

a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'b'), (7, 'c'), (8, 'd'), (9, 'e')]

shuffle(a)
# tr = bst.bst(a, randomize=True)
avltr = bst.AVLtree(a)
print avltr.inorderTreeWalk()