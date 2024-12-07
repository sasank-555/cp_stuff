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
    n,m,d = LII()
    p = LGLII()
    adj = defaultdict(list)
    for _ in range(n-1):
        x,y = LGLII()
        adj[x].append(y)
        adj[y].append(x)
    dp = [[-1, -1] for _ in range(n)]
    st = []
    affected = [0] * n
    for node in p:
        affected[node] = 1
    parent =[-1]*n
    while st:
        u = st.pop()
        if u>=0:
            st.append(~u)
            for v in adj[u]:
                if v!=parent[u]:
                    parent[v] = u 
                    st.append(v)
        else:
            u = ~u
            if affected[u]:
                dp[u] = [0,0]
            for v in adj[u]:
                if v!=parent[u]:
                    if dp[v][0]!=-1:
                        dist = dp[v][0] + 1
                        if dist> dp[u][0] :
                            dp[u][1] = dp[u][0]
                            dp[u][0] = dist
                        elif dist>dp[u][1]:
                            dp[u][1] = dist
    ndp = dp[:]
    st  = [0]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v!=parent[u]:
                if 1 + dp[v][0]==ndp[u][0]:
                    ndp[v] = [1 + dp[v][0] , max(ndp[u][1]+ 1,dp[v][1])]
                else:
                    ndp[v] = list(nlargest(2,[1 + ndp[u][0],dp[v][1],dp[v][0],1 + ndp[u][1]]))[::-1]
                parent[v] = u
                st.append(v)
    print(ndp)             
    return sum([1 for i in range(n) if ndp[i][0]<=d and ndp[i][0]!=-1])   
t  = solve()
print(t)