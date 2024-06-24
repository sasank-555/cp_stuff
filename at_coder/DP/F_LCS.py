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
# def helper(i,j):
#   if i==len(s) or j==len(t):return 0
#   if s[i]==t[j]:
#     return 1 + helper(i+1,j+1)
#   return max(helper(i+1,j),helper(i,j+1))
ans = []
s= I()
t = I()
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for i in reversed(range(len(s))):
  for j in reversed(range(len(t))):
    if s[i]==t[j]:
      dp[i][j] = 1 + dp[i+1][j+1]
    else:
      dp[i][j] = max(dp[i+1][j],dp[i][j+1])
# def printSol(i,j):
#   if i==len(s) or j==len(t):return
#   if s[i]==t[j]:
#     ans.append(s[i])
#     printSol(i+1,j+1)
#   else:
#     if dp[i+1][j] > dp[i][j+1]:
#       printSol(i+1,j)
#     else:
#       printSol(i,j+1)
i,j = 0,0
while i<len(s) and j<len(t):
  if s[i]==t[j]:
    ans.append(s[i])
    i+=1
    j+=1
  elif dp[i+1][j] > dp[i][j+1]:
    i+=1
  else:
    j+=1

print("".join(ans))

