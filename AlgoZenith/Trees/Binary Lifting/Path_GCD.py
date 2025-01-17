########################################################################################################################
# -----------------------------------------------AUTHOR: shank_555-----------------------------------------------------#
########################################################################################################################
import time
from bisect import bisect_left,bisect_right
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
class SafeCounter(Counter):
    """
    A Counter subclass that obfuscates keys using a random 64-bit integer to prevent hash collision attacks.
    
    Only supports integer keys by default. Other key types can be supported by converting them to integers.
    """
    def __init__(self, *args, r64=None, **kwargs):
        self.r64 = r64 or random.getrandbits(64)  # Generate a 64-bit random integer if not provided
        super().__init__(*args, **kwargs)

    def _transform_key(self, key):
        """Apply an XOR-based transformation to the key."""
        if not isinstance(key, int):
            raise TypeError(f"SafeCounter only supports integer keys, got {type(key)}.")
        return key ^ self.r64

    def __setitem__(self, key, value):
        transformed_key = self._transform_key(key)
        super().__setitem__(transformed_key, value)

    def __delitem__(self, key):
        transformed_key = self._transform_key(key)
        super().__delitem__(transformed_key)

    def __getitem__(self, key):
        transformed_key = self._transform_key(key)
        return super().__getitem__(transformed_key)

    def __contains__(self, key):
        transformed_key = self._transform_key(key)
        return super().__contains__(transformed_key)
def input(): return sys.stdin.readline().rstrip("\r\n")
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
from math import gcd
inf = float('inf')
def solve():
    n = II()
    val =[0] +  LII()
    adj =[[] for _ in range(n + 1)]
    for _ in range(n-1):
        u,v = LII()
        adj[u].append(v)
        adj[v].append(u)
    LOG  = n.bit_length() + 1
    par = [[0]*LOG for _ in range(n + 1)]
    dp = [[0]*LOG for _ in range(n + 1)]
    st = [(1 , 0)] 
    lvl = [0]*(n + 1)
    while st:
        u ,d = st.pop()
        lvl[u] = d
        for v in adj[u]:
            if par[u][0]!=v:
                par[v][0] = u
                dp[v][0] = val[v]
                st.append((v ,1 + d))
    for j in range(1,LOG):
        for u in range(1, n + 1):
            par[u][j] = par[par[u][j-1]][j-1]
            dp[u][j] = gcd(dp[u][j-1],dp[par[u][j-1]][j-1])
    def query(u,v):
        if lvl[u] < lvl[v]:
            u,v = v,u
        ans = 0
        for i in range(LOG-1,-1,-1):
            if (lvl[u] - lvl[v])&(1<<i):
                ans = gcd(ans,dp[u][i])
                u = par[u][i]
        if u==v:
            return gcd(ans,val[u])
        for i in range(LOG-1,-1,-1):
            if par[u][i]!=par[v][i]:
                ans = gcd(ans,dp[u][i])
                ans = gcd(ans,dp[v][i])
                u = par[u][i]
                v = par[v][i]
        ans = gcd(ans,gcd(val[v],val[u]))
        return gcd(ans,val[par[v][0]])
    q = II()
    for _ in range(q):
        u,v = LII()
        print(query(u,v))
for _ in range(II()):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")