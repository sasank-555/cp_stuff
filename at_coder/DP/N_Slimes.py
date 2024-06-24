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

def helper(l,r):
  if l==r:
    return 0
  if dp[l][r]!=-1:
    return dp[l][r]
  dp[l][r] = inf
  for j in range(l,r):
    dp[l][r] = min(dp[l][r], prefix[r]-(prefix[l-1] if l>0 else 0) + helper(l,j)+helper(j+1,r))
  return dp[l][r]
dp = [[-1]*401 for _ in range(401)]
N = II()
a = LII()
prefix  = a [:]
for i in range(1,N):
  prefix[i]+=prefix[i-1]
print(helper(0,N-1))

