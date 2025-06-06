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
class node:
    def __init__(self):
        self.s =  0
        self.mxs = 0
        self.ps = 0
        self.ss = 0
def combine(n1,n2,ret):
    ret.s = n1.s + n2.s
    ret.ps = max(n1.s + n2.ps , n1.ps)
    ret.ss = max(n2.ss,n2.s + n1.ss)
    ret.mxs = max(n1.mxs,n2.mxs,n1.ss + n2.ps)
    return ret
def solve():
    n,q = LII()
    nums = LII()
    tree = [node() for _ in range(4*n)]
    def build(v, tl, tr):
        if tl == tr:
            tree[v].s = nums[tl]
            tree[v].ps = nums[tl]  
            tree[v].ss = nums[tl]
            tree[v].mxs = nums[tl]
            return
        mid = (tl + tr) // 2
        build(2 * v + 1, tl, mid)
        build(2 * v + 2, mid + 1, tr)
        combine(tree[2 * v + 1], tree[2 * v + 2],tree[v])
    def update(v,tl,tr,i,val):
        if tl==tr:
            tree[v].s = val
            tree[v].ps = val
            tree[v].ss = val
            tree[v].mxs = val
            return 
        mid = (tl + tr)//2
        if i<=mid:
            update(2*v + 1,tl,mid,i,val)
        else:
            update(2*v + 2 , mid + 1,tr,i,val)
        combine(tree[2*v + 1], tree[2*v + 2],tree[v])
    build(0,0,n-1)
    for _ in range(q):
        i,val = LII()
        i-=1
        update(0,0,n-1,i,val)
        print(max(0,tree[0].mxs))
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
