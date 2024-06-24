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
@lru_cache(None)
def helper(i,j):
  if i==N:
    return int(j==k)
  ans = 0
  # see for every j u need below row's sum for j...j+a[i] so use a prefix sum to store it
  for m in range(0,a[i]+1):
    ans+= helper(i+1,j+m)
  return ans
N,k = LII()
a = LII()
dp = [[0]*(k+1) for _ in range(N+1)]
for i in range(N+1):
  dp[i][k]=1
for i in reversed(range(N)):
  pre = dp[i+1][:]
  for j in range(1,k+1):
    pre[j]+=pre[j-1]
  for j in reversed(range(k)):
    ans = pre[min(j+a[i],k)] - (pre[j-1] if j>0 else 0)
    dp[i][j]=ans

print(dp[0][0]%MOD1)