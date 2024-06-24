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
import sys
sys.setrecursionlimit(10**6)
def dfs(i,j):
  if i==H-1 and j==W-1:
    return 1
  if vis[i][j]:
    return dp[i][j]
  vis [i][j] = 1
  a = 0
  if i+1<H and grid[i+1][j]!="#":
    a = dfs(i+1,j)
  b  = 0 
  if j+1<W and grid[i][j+1]!="#":
    b = dfs(i,j+1)
  dp[i][j] =  a+b
  return dp[i][j]
H , W  =LII()
grid = [list(I()) for _ in range(H)]
vis = [[0]*W for _ in range(H)]
dp = [[0]*W for _ in range(H)]
print(dfs(0,0)%MOD1)


    