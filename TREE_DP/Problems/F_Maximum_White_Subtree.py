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
    n = II()
    a = LII()
    adj = defaultdict(list)
    for _ in range(n-1):
        x,y = LII()
        x-=1
        y-=1
        adj[x].append(y)
        adj[y].append(x)
    a = [1 if x==1 else -1 for x in a]
    dp = [0]*n
    st = [0]
    parent = [-1]*n
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
            dp[u] = a[u]
            for v in adj[u]:
                if v!=parent[u]:
                    dp[u]+=max(0,dp[v])
    ndp  = [0]*n
    ndp[0] = dp[0]
    ans =[-1]*n
    st = [0]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v!=parent[u]: 
                ndp[v] = max(0,ndp[u]-max(0,dp[v])) + dp[v]
                st.append(v)
    return ndp



    
            

t  = solve()
print(*t)