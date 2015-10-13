#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2014-12-13 22:08:04
# @Last Modified by:   Athul
# @Last Modified time: 2015-09-12 10:37:45

from sorty import sorty
import random

a = list(xrange(50))
random.shuffle(a)
print(a)
b = sorty.quickSort(a)
print(b)
