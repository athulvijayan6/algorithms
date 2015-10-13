#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: athul
# @Date:   2015-10-09 15:12:52
# @Last Modified by:   athul
# @Last Modified time: 2015-10-09 23:49:41
def BFS(G, s):
    status = {}
    for u in G.keys():
        status[u] = [False, None, -1] # visited?, parent, du, fu, distance
    status[s][0] = True
    status[s][2] = 0
    q = Queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not status[v][0]:    # if not visited
                status[v][0] = True
                status[v][1] = u
                status[v][2] = status[u][4] + 1
                q.put(v)
    return status

def BellmanFord(G, W, s):
    dist = {v:[float('inf'), None] for v in G.keys()}  #Distance, parent
    dist[s][0] = 0
    for i in xrange(len(G.keys())-1):
        for u in G.keys():
            for v in G[u]:
                # (u, v) is an edge
                if dist[v][0] > dist[u][0] + W[u][v]:
                    dist[v][0] = dist[u][0] + W[u][v]:
                    dist[v][1] = u
    for u in G.keys():
        for v in G[u]:
            if dist[v][0] > dist[u][0] + W[u][v]:
                return False
    return dist

def dijkstra(G, W, s):
    dist = {v:[float('inf'), None] for v in G.keys()}  #Distance, parent
    dist[s][0] = 0



    