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
import sys
sys.setrecursionlimit(2*(10**6) + 1)
inf = float('inf')
res = [0]*(2*((10**6) +1))
subSize = [0]*(2*((10**6) +1))
subDist = [0]*(2*((10**6) +1))
def dfs1(i,p):
  subSize[i] = 1
  for v in adj[i]:
    if v!=p:
      dfs1(v,i)
      subSize[i]+=subSize[v]
      subDist[i] += subSize[v] + subDist[v]
def dfs(i,p):
  res[i] = res[p] - subSize[i] - subDist[i] + n - subSize[i] + subDist[i]
  for v in adj[i]:
    if v!=p:
      dfs(v,i)
n = II()
adj = defaultdict(list)
for _ in range(n-1):
  a,b  = LII()
  adj[a].append(b)
  adj[b].append(a)

dfs1(1,-1)
res[1] = subDist[1]
for v in adj[1]:
  dfs(v,1)
for i in range(1,n+1):
  print(res[i],end=" ")
print()