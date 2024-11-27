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
alphabets = list("abcdefghijklmnopqrstuvwxyz")
vowels = list("aeiou")
MOD1 = int(1e9 + 7)
MOD2 = 998244353
INF = int(1e17)
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
inf = float('inf')
def solve():
    n,m = LII()
    adj = defaultdict(list)
    for _ in range(m):
        x,y = LII()
        adj[x].append(y)
        adj[y].append(x)
    q = deque()
    vis = set()
    vis.add(1)
    q.append((0,1))
    parent = defaultdict(int)
    parent[1]  = -1
    while q:
        d, node  = q.popleft()
        if node==n:
            return d,parent,n
        for x in adj[node]:
            if x not in vis:
                vis.add(x)
                parent[x] = node
                q.append((d + 1,x))
    return -1,parent,n


t,p,n  = solve()
if t==-1:
    print("IMPOSSIBLE")
else:
    print(t + 1)
    path = []
    curr = n
    while curr!=-1:
        path.append(curr)
        curr = p[curr]
    print(*path[::-1])