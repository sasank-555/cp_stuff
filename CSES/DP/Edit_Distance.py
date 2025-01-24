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
inf = float('inf')
def solve():
    s = I()
    t = I()
    # has_dp =[[False]*(len(t) + 1) for _ in range(len(s) + 1) ] 
    dp = [[-1]*(len(t) + 1) for _ in range(len(s) + 1) ]
    # def go(i,j):
    #     if j==len(t):
    #         return len(s) - i
    #     if i==len(s):
    #         return len(t) - j
    #     if has_dp[i][j]:
    #         return dp[i][j]
    #     has_dp[i][j] = True
    #     if s[i]==t[j]:
    #         dp[i][j] = go(i + 1, j + 1)
    #         return dp[i][j]
    #     dp[i][j] =  1 + min(go(i,j+1),go(i + 1,j),go(i + 1,j + 1))
    #     return dp[i][j]
    for i in range(len(s),-1,-1):
        for j in range(len(t),-1,-1):
            if j==len(t):dp[i][j] = len(s) - i
            elif i==len(s) : dp[i][j] = len(t) - j
            else:
                if s[i]==t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j] , dp[i+ 1][j + 1], dp[i][j + 1])
        
    
    return dp[0][0]
for _ in range(1):
    t  = solve()
    print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
