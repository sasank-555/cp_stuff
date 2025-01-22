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
maxn = 10**6
# dp =[[0]*(3) for _ in range(maxn + 1)]
# for i in range(maxn,-1,-1):
#     for j in range(3):
#         if i==maxn:
#             dp[i][j]= 1
#             continue
#         dp[i][j]+=dp[i + 1][1] + dp[i + 1][2]
#         if j==1:
#             dp[i][j]+=dp[i + 1][1]*3
#         if j==2:
#             dp[i][j]+=dp[i + 1][2]
#         dp[i][j]%=MOD1
dp =[[-1]*(3) for _ in range(maxn + 1)]
def go(i,l):
    if i==maxn:
        return 1
    if dp[i][l]!=-1:
        return dp[i][l]
    a = go(i + 1, 1) + go(i + 1, 2) 
    a%=MOD1
    if l==1:
        a+=go(i + 1,1)*3
        a%=MOD1
    if l==2:
        a+=go(i + 1,2)
        a%=MOD1
    dp[i][l] = a
    return dp[i][l]
for i in range(maxn,-1,-1):
    for j in range(3):
        go(i,j)
for _ in range(II()):
    n = II()
    print(go(maxn-n,0))
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")