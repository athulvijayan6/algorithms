#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2014-10-13 13:16:40
# @Last Modified by:   Athul Vijayan
# @Last Modified time: 2014-10-16 10:22:21
memo = {};
def memoize(n):
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = memoize(n-1) + memoize(n-2)
        memo[n] = f
    return f

def naive(n):
    if n <= 2:
        f = 1
    else:
        f = naive(n-1) + naive(n-2)
    return f
