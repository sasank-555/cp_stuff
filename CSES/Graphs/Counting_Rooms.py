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
dirs = [[0,1],[1,0],[-1,0],[0,-1]]
sys.setrecursionlimit(2*(10**5))
def solve():
    n,m = LII()
    grid = []
    for _ in range(n):
        grid.append(list(I()))
    def dfs(i,j):
        vis[i][j] = True
        for di,dj in dirs:
            ni = i + di 
            nj = j + dj
            if 0<=ni<n and 0<=nj<m and not vis[ni][nj] and grid[ni][nj]==".":
                dfs(ni,nj)
    vis = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
           if not vis[i][j] and grid[i][j]==".":
               dfs(i,j)
               cnt+=1
    return cnt     
        

t  = solve()
print(t)