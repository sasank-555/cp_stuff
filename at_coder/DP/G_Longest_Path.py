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
sys.setrecursionlimit(10**6)
def dfs(i):
  if vis[i]:
    return dp[i]
  vis[i] = 1
  ans = 0
  for v in adj[i]:
    ans = max(ans,1+dfs(v))
  dp[i] = ans
  return ans
N,M  = LII()
adj = defaultdict(list)
edges = [LII() for _ in range(M)]
for x, y in edges:
  adj[x].append(y)
dp = [0]*(N+1)
vis = [0]*(N+1)
for i in range(1,N+1):
  if not vis[i]:
    dfs(i)
print(max(dp))