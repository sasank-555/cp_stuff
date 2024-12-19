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
    n, most = LII()
    nums = [LII() for _ in range(n)]
    
    # dp = set()
    # dp.add((0,0))
    # for w,v in nums:
    #     ndp = set()
    #     ndp.add((w,v))
    #     for nw , nv in dp:
    #         if nw + w<=most:
    #             ndp.add((nw + w,nv + v))
    #     dp = dp | ndp
    # return max(y for x,y in dp) 
    dp = Counter()
    dp[0] = 0
    for w,v in nums:
        ndp = Counter()
        for nw in dp:
            if nw + w<=most:
                ndp[nw + w] = max(ndp[nw + w],dp[nw] + v)
        for x in range(most + 1):
            dp[x] = max(dp[x] , ndp[x])
    return max(dp.values()) 
for _ in range(1):
    t = solve()
    print(t)
