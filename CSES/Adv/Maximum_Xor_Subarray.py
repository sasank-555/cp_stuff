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
class Node:
    def __init__(self):
        self.children = {}
def solve():
    n = II()
    nums  = LII()
    p = [0]
    for x in nums:
        p.append(p[-1] ^ x)
    root = Node()
    def insert(val):
        curr = root
        for i in reversed(range(32)):
            bit = 1 if val & (1<<i) else 0
            if bit in curr.children:curr = curr.children[bit]
            else:
                curr.children[bit] = Node()
                curr = curr.children[bit]
    def gemx(val):
        curr = root
        ans = 0
        for i in reversed(range(32)):
            bit = 1 if val & (1<<i) else 0
            if 1^bit in curr.children:
                ans+=(1<<i)
                curr = curr.children[1^bit]
            elif bit in curr.children:
                curr = curr.children[bit]
            else:
                break
        return ans    
    root = Node()      
    mx = 0
    for i in range(len(p)):
        mx = max(mx , gemx(p[i]))
        insert(p[i])
    print(mx)
for i in range(7,10000,7):
    if str(i)[-1]=="7":
        print(i,sum(map(int,str(i))))
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
