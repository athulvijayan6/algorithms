#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2015-10-09 15:13:15
# @Last Modified by:   athul
# @Last Modified time: 2015-10-09 16:13:12
from graphs import explore

nV, nE = 9, 5
V = list(xrange(nV))
G = {u:[] for u in V}
directed = False

E = [(0, 1), (0, 4), (1, 2), (1, 4), (2, 5), (4, 5), (5, 8), (3, 6), (3, 7), (6, 7)]
for edge in E:
    G[edge[0]].append(edge[1])
    if not directed:
        G[edge[1]].append(edge[0])

status = explore.BFS(G, 0)