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
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]  

def solve():
    n, m = map(int, input().split()) 
    grid = [list(input()) for _ in range(n)]  

    vis = [[False] * m for _ in range(n)] 
    parent = {} 
    d = {(0, 1): "R", (0, -1): "L", (1, 0): "D", (-1, 0): "U"}  

    def bfs(si, sj):
        queue = deque([(si, sj)]) 
        vis[si][sj] = True
        while queue:
            i, j = queue.popleft()
            if grid[i][j] == "B": 
                return i, j
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and not vis[ni][nj] and grid[ni][nj] != "#":
                    vis[ni][nj] = True
                    queue.append((ni, nj))
                    parent[(ni, nj)] = (i, j)  
        return -1, -1  

    si, sj, bi, bj = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "A":
                si, sj = i, j
            elif grid[i][j] == "B":
                bi, bj = i, j

    ei, ej = bfs(si, sj) 
    if (ei, ej) == (-1, -1):  
        print("NO")
        return

    path = []
    cur = (ei, ej)
    while cur != (si, sj):
        prev = parent[cur]
        di, dj = cur[0] - prev[0], cur[1] - prev[1]
        path.append(d[(di, dj)])
        cur = prev

    path.reverse()  
    print("YES")
    print(len(path))
    print("".join(path))

solve()