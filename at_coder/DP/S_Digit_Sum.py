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
sys.setrecursionlimit(10001)
def solve():
    r = I()
    l = 1
    d = II()
    def erap(s):
      N = len(s)
      dp =[[[-1]*(d) for _ in range(2)] for _ in range(N + 1)]
      # @lru_cache(None)
      def go(idx,tight,rem):
         if dp[idx][tight][rem]!=-1:
            return dp[idx][tight][rem]
         if idx==N:
            return int(rem==0)
         md = 9 if not tight else int(s[idx])
         ans = 0
         for j in range(md + 1):
            ans+=go(idx + 1, tight and j==int(s[idx]), (rem + j)%d)
            ans%=MOD1
         dp[idx][tight][rem] = ans 
         return ans 
      r = go(0,True,0)
      # go.cache_clear()
      return r
    return (erap(r) - 1)%MOD1
for _ in range(1):
    t  = solve()
    print(t)