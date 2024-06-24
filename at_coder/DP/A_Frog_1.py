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
# @lru_cache(None)
# def helper(i):
#   if i==N-1:
#     return 0
#   one  = abs(h[i]-h[i+1]) + helper(i+1)
#   two = inf
#   if i+2<=N-1:
#     two = abs(h[i]-h[i+2]) + helper(i+2)
#   return min(one,two)

# helper.cache_clear()
N = II()
h = LII()
# print(helper(0))
dp  = [0]*(N)
for i in reversed(range(N-1)):
  one  = abs(h[i]-h[i+1]) + dp[i+1]
  two = inf
  if i+2<=N-1:
    two = abs(h[i]-h[i+2]) + dp[i+2]
  dp[i] =  min(one,two)
print(dp[0])
