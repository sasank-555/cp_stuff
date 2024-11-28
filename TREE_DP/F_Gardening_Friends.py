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
    n, k, c = LII()  
    adj = defaultdict(list)

    for _ in range(n - 1):
        x, y = LGLII()
        adj[x].append(y)
        adj[y].append(x)

    largest = [0] * n
    second = [0] * n
    parent = [-1] * n
    st = [0]

    while st:
        u = st.pop()
        if u >= 0:
            st.append(~u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    st.append(v)
        else:
            u = ~u
            a = b = 0
            for v in adj[u]:
                if v != parent[u]:
                    x = 1 + largest[v]
                    if x >= a:
                        a, b = x, a
                    elif x >= b:
                        b = x
            largest[u] = a
            second[u] = b

    st = [(0, 0)] 
    ans = largest[:]

    while st:
        u, d = st.pop()
        ans[u] = max(ans[u], d)
        for v in adj[u]:
            if v != parent[u]:
                x = 1 + largest[v]
                a, b = largest[u], second[u]
                nex = d
                if x == a:
                    nex = max(nex, b)
                else:
                    nex = max(nex, a)
                st.append((v, 1 + nex))

    best = 0
    st = [(0, 0)]  

    while st:
        u, d = st.pop()
        best = max(best, (k * ans[u] - d*c))
        for v in adj[u]:
            if v != parent[u]:
                st.append((v, d + 1))
    return best
for _ in range(II()):
    t  = solve()
    print(t)