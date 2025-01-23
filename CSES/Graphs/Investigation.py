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
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a,b,c = LII()
        adj[a].append((b,c))
    dp =[inf]*(n + 1)
    dp[1] = 0
    cnt = [0]*(n + 1)
    mx = [0]*(n + 1)
    mi = [0]*(n + 1)
    q = [(0,1)]
    cnt[1] = 1
    while q:
        cost, node =  heappop(q)
        if cost > dp[node] : continue
        for v,w in adj[node]:
            if dp[v] > cost + w:
                dp[v] = dp[node] + w
                mi[v] = mi[node] + 1
                mx[v] = mx[node] + 1
                cnt[v] = cnt[node]
                heappush(q,(dp[v],v))
            elif dp[v]==cost + w:
                cnt[v]+=cnt[node]
                cnt[v]%=MOD1
                mi[v] = min(mi[v] ,mi[node] + 1,mx[node] + 1)
                mx[v] = max(mx[v],mi[node] + 1,mx[node] + 1)
    if dp[n]==inf:
        print(-1)
    else:
        print(dp[n] , cnt[n],mi[n],mx[n])  
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
