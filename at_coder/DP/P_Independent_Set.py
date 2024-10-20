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
sys.setrecursionlimit(1000000)
N = II()
adj = defaultdict(list)
dp_white = [1]*N
dp_black = [1]*N

def dfs(v, p):
  for c in adj[v]:
    if c==p:
      continue
    dfs(c, v)
    dp_white[v] *= dp_white[c]+dp_black[c]
    dp_black[v] *= dp_white[c]
    dp_white[v] %= MOD1
    dp_black[v] %= MOD1
for _ in range(N-1):
  x,y = LII()
  x-=1
  y-=1
  adj[x].append(y)
  adj[y].append(x)
dfs(0,-1)
print((dp_white[0]+dp_black[0])%MOD1)

    