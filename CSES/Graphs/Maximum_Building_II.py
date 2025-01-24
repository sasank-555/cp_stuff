########################################################################################################################
# -----------------------------------------------AUTHOR: shank_555-----------------------------------------------------#
########################################################################################################################
import time
from bisect import bisect_left,bisect_right
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
def input(): return sys.stdin.readline().rstrip("\r\n")
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
def solve():
    n,m = LII()
    grid = [I() for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    ans =[[0]*(n + 1) for _ in range(m)]
    for j in range(m):
        dp[n-1][j] = 1 if grid[n-1][j] =="." else 0
    for i in range(n-2,-1,-1):
        for j in range(m):
            if grid[i][j]=="*":
                dp[i][j] = 0
                continue
            dp[i][j]= 1 + dp[i + 1][j]
    ret = 0
    for i in range(n):
        for length in range(1,m + 1):
            dq = deque()  
            for r in range(len(dp[i])): 
                if dq and dq[0] < r - length + 1:
                    dq.popleft()
                while dq and dp[i][dq[-1]] >= dp[i][r]:
                    dq.pop()
                dq.append(r)
                if r >= length - 1:
                    mi = dp[i][dq[0]]  
                    ans[length - 1][0] += 1
                    ans[length - 1][mi] -= 1
    for i in range(m):
        ans[i].pop()
        for j in range(1,n):
            ans[i][j]+=ans[i][j-1]
    for x in zip(*ans):print(*x)
        # ret+= calculate_total_sum(dp[i])
    # print(ret)
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
