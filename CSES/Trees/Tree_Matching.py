# ███████╗ █████╗ ███████╗ █████╗ ███╗   ██╗██╗  ██╗
# ██╔════╝██╔══██╗██╔════╝██╔══██╗████╗  ██║██║ ██╔╝
# ███████╗███████║███████╗███████║██╔██╗ ██║█████╔╝ 
# ╚════██║██╔══██║╚════██║██╔══██║██║╚██╗██║██╔═██╗ 
# ███████║██║  ██║███████║██║  ██║██║ ╚████║██║  ██╗
# ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                                       
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
inf = float('inf')
def solve():
    N = II()
    adj  = [[] for _ in range(N)]
    for _ in range(N -1):
        x,y = LGLII()
        adj[x].append(y)
        adj[y].append(x)
    dp =[[-1]*2 for _ in range(N)]
    def go(node,p,t):
        if dp[node][t]!=-1:
            return dp[node][t]
        if t==1:
            ans = 0
            for v in adj[node]:
                if v!=p:
                    go(v,node,0)
                    ans+=dp[v][0]
        else:
            ans = 0
            for v in adj[node]:
                if v!=p:
                    go(v,node,0)
                    ans+=dp[v][0]
            ans2 = 0
            for v in adj[node]:
                if v!=p:
                    go(v,node,1)
                    ans2 = max(ans2 , 1 + dp[v][1] + ans - dp[v][0])
            ans = max(ans,ans2)
        dp[node][t] = ans          

for _ in range(1):
    t  = solve()
    print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")