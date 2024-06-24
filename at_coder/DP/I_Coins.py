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
@lru_cache(None)
def helper(i,h):
  if i==N:
    t = N-h
    return int(h>t)
  return p[i]*helper(i+1,h+1) + (1-p[i])*helper(i+1,h)
N  = II()
p = list(map(float,I().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
for i in reversed(range(N+1)):
  for h in reversed(range(N+1)):
    if i==N:
      t = N- h
      dp[i][h] = int(h>t)
    elif h==N:
      dp[i][h] = 1
    else:
      dp[i][h] = p[i]*dp[i+1][h+1] + (1-p[i])*dp[i+1][h]
print(dp[0][0])