#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2015-10-09 15:12:10
# @Last Modified by:   athul
# @Last Modified time: 2015-10-09 16:12:39
import Queue

def DFSvisit(G, status, u, time):
    status[u][0] = True
    time += 1
    status[u][2] = time
    for v in G[u]:
        if not status[v][0]:  # if not visited
            status[v][1] = u
            status, time = DFSvisit(G, status, v, time)
    status[u][3] = time
    return status, time


def DFS(G):
    status = {}
    for u in G.keys():
        status[u] = [False, None, None, None] # visited?, parent, du, fu
    time = 0
    for u in G.keys():
        if not status[u][0]:  # if not visited
            status, time = DFSvisit(G, status, u, time)
    return status

def BFS(G, s):
    status = {}
    for u in G.keys():
        status[u] = [False, None, None, None, -1] # visited?, parent, du, fu, distance
    time = 0
    status[s][0] = True
    status[s][2] = time
    status[s][4] = 0
    q = Queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        status[u][2] = time
        for v in G[u]:
            if not status[v][0]:    # if not visited
                status[v][0] = True
                status[v][1] = u
                status[v][4] = status[u][4] + 1
                q.put(v)
                time += 1
        status[u][3] = time
    return status



