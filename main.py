#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2014-10-13 16:21:22
# @Last Modified by:   Athul Vijayan
# @Last Modified time: 2014-10-18 12:35:32

import fibonacci
from timeit import default_timer as timer
from tabulate import tabulate

table = [["Algorithm", "n", "f(n)", "runTime"]]
for n in [10000]:
    # start = timer()
    # f = fibonacci.naive(n)
    # end = timer()
    # table.append(["naive", n, f, end-start])

    start = timer()
    f = fibonacci.memoize(n)
    end = timer()
    table.append(["memoize", n, f, end-start])

print tabulate(table)

