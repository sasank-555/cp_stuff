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
def solve():
    n,m = LII()
    adj = defaultdict(list)
    for _ in range(m):
        x,y,w = LII()
        adj[x].append((y,w))
    q = []
    dis = [inf]*(n+1)
    dis[1]  = 0
    heappush(q,(0,1))
    while q:
        d, node  =heappop(q)
        if dis[node] < d:
            continue
        for v,w in adj[node]:
            if dis[v] > w  + d:  
              dis[v] = d + w
              heappush(q,(d + w,v))
    print(*dis[1:])
                

t  = solve()