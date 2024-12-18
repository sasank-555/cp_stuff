########################################################################################################################
# -----------------------------------------------AUTHOR: shank_555-----------------------------------------------------#
########################################################################################################################
import time
import bisect
import functools
import math
import os
import random
import re
import sys
import threading
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from io import BytesIO, IOBase
from itertools import accumulate, combinations, permutations
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase
from typing import *
import collections
import heapq
import itertools
input = sys.stdin.readline
alphabets = list("abcdefghijklmnopqrstuvwxyz")
vowels = list("aeiou")
MOD1 = int(1e9 + 7)
MOD2 = 998244353
INF = int(1e17)
input = sys.stdin.readline
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
inf = float('inf')
def exclusive(A, zero, combine, node):
    n = len(A)
    exclusiveA = [zero] * n # Exclusive segment tree
 
    # Build exclusive segment tree
    for bit in range(n.bit_length())[::-1]:
        for i in range(n)[::-1]:
            # Propagate values down the segment tree    
            exclusiveA[i] = exclusiveA[i // 2]
        for i in range(n & ~int(bit == 0)):
            # Fold A[i] into exclusive segment tree
            ind = (i >> bit) ^ 1
            exclusiveA[ind] = combine(exclusiveA[ind], A[i], node, i)
    return exclusiveA
 
def rerooter(graph, default, combine, finalize = lambda nodeDP,node,eind: nodeDP):
    n = len(graph)
    rootDP = [0] * n
    forwardDP = [None] * n
    reverseDP = [None] * n
 
    # Compute DP for root=0
    DP = [0] * n
    bfs = [0]
    P = [0] * n
    for node in bfs:
        for nei in graph[node]:
            if P[node] != nei:
                P[nei] = node
                bfs.append(nei)
 
    for node in reversed(bfs):
        nodeDP = default[node]
        for eind, nei in enumerate(graph[node]):
            if P[node] != nei:
                nodeDP = combine(nodeDP, DP[nei], node, eind)
        DP[node] = finalize(nodeDP, node, graph[node].index(P[node]) if node else -1)
    # DP for root=0 done
    
    # Use the exclusive function to reroot 
    for node in bfs:
        DP[P[node]] = DP[node]
        forwardDP[node] = [DP[nei] for nei in graph[node]]
        rerootDP = exclusive(forwardDP[node], default[node], combine, node)
        reverseDP[node] = [finalize(nodeDP, node, eind) for eind, nodeDP in enumerate(rerootDP)]
        rootDP[node] = finalize((combine(rerootDP[0], forwardDP[node][0], node, 0) if n > 1 else default[node]), node, -1)
        for nei, dp in zip(graph[node], reverseDP[node]):
            DP[nei] = dp
    return rootDP, forwardDP, reverseDP
def solve():
    n = II()
    P = [int(x) - 1 for x in input().split()]
    graph = [[] for _ in range(n)]
    for v in range(1, n):
        u = P[v - 1]
        graph[u].append(v)
        graph[v].append(u)

    default = [1]*n
    def combine(nodeDP, neiDP, node, eind):
        return nodeDP * neiDP % MOD1
    
    def finalize(nodeDP, node, eind):
        return (nodeDP + (eind != -1)) % MOD1
    print(*rerooter(graph,default,combine,finalize)[0])
    
for _ in range(1):
    t  = solve()