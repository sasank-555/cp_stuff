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
    N,q = LII()
    nums = LII()
    d = defaultdict(list)
    for i,x in enumerate(nums):d[x].append(i)
    for i,x in enumerate(nums):
        j = bisect_right(d[x],i)
        if j==len(d[x]):
            nums[i] = N + 1
        else:
            nums[i] =  d[x][j]  +  1
    queries = [LII() for _ in range(q)]
    for i in range(q):
        queries[i].append(i)
    queries.sort(key = lambda x : -x[1])
    nums = sorted([[x,i] for i,x in enumerate(nums)])
    tree = [0]*(N + 1)
    def update(i):
        i+=1
        while i<len(tree):
            tree[i]+=1
            i+=(i & -i)
    def query(i):
        i+=1
        ret = 0
        while i > 0:
            ret+=tree[i]
            i-=(i & -i)
        return ret
    j = len(nums) - 1
    ans = [0]*(q)
    # print(nums)
    # print(queries)
    for l,r,i in queries:
        while j>=0 and nums[j][0] > r:
            update(nums[j][1])
            j-=1
        r-=1
        l-=1
        ans[i] = query(r) - query(l-1)
    for x in ans:
        print(x)
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
