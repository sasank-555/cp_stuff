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
sys.setrecursionlimit(10**9)
@lru_cache(None)
def helper(i,j,turn):
  if i==j:
    return a[i] if turn==0 else 0
  if turn==0:
    return max(a[i]+helper(i+1,j,1),a[j]+helper(i,j-1,1))
  else:
    return min(helper(i+1,j,0),helper(i,j-1,0))


N = II()
a = LII()


dp = [[[0] * 2 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i][0] = a[i]

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j][0] = max(a[i] + dp[i + 1][j][1], a[j] + dp[i][j - 1][1])
        dp[i][j][1] = min(dp[i + 1][j][0], dp[i][j - 1][0])
total_sum = sum(a)
print (2 * dp[0][N - 1][0] - total_sum)