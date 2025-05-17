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
class SegmentTree:
    def __init__(self, nums, fn=min):
        self.n = len(nums)
        self.fn = fn
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, index, low, high):
        if low == high:
            self.tree[index] = nums[low]
        else:
            mid = (low + high) // 2
            self.build(nums, 2 * index + 1, low, mid)
            self.build(nums, 2 * index + 2, mid + 1, high)
            self.tree[index] = self.fn(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def rangeQuery_(self, index, low, high, left, right):
        if low >= left and high <= right:
            return self.tree[index]
        elif low > right or high < left:
            if self.fn == min:
                return float('inf')
            elif self.fn == max:
                return float('-inf')
            else:
                return 0
        else:
            mid = (low + high) // 2
            l = self.rangeQuery_(2 * index + 1, low, mid, left, right)
            r = self.rangeQuery_(2 * index + 2, mid + 1, high, left, right)
            return self.fn(l, r)

    def rangeQuery(self, left, right):
        return self.rangeQuery_(0, 0, self.n - 1, left, right)

    def update_(self, i, val, index, low, high):
        if low == high:
            self.tree[index] = val
            return
        mid = (low + high) // 2
        if i > mid:
            self.update_(i, val, 2 * index + 2, mid + 1, high)
        else:
            self.update_(i, val, 2 * index + 1, low, mid)
        self.tree[index] = self.fn(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def update(self, i, val):
        return self.update_(i, val, 0, 0, self.n - 1)
def solve():
    N,Q = LII()
    nums = LII()
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        x,y = LGLII()
        adj[x].append(y)
        adj[y].append(x)
    parent = [-1]*N
    st = [0]
    timer = -1
    intime = [0]*N
    outtime = [0]*N
    vals = [0]*(2*N)
    while st:
        u = st.pop()
        if u>=0:
            timer+=1
            intime[u] = timer
            vals[timer] = nums[u]
            st.append(~u)
            for v in adj[u]:
                if v!=parent[u]:
                    st.append(v)
                    parent[v]  = u
        else:
            u = ~u
            timer+=1
            # vals[timer] = -nums[u]
            outtime[u]  = timer
            
    # print(vals)
    # print(intime,outtime)
    st = SegmentTree(vals,fn = lambda x,y : x + y)
    for _ in range(Q):
        ahh = LII()
        if ahh[0]==1:
            idx = intime[ahh[1] - 1]
            st.update(idx,ahh[2])
        else:
            l = intime[ahh[1] - 1]
            r = outtime[ahh[1]  - 1]
            # print(l,r)
            print(st.rangeQuery(l,r))
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
