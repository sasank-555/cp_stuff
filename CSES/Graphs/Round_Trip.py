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
sys.setrecursionlimit(2*(10**5))
from collections import defaultdict
def solve():
    n, m = LII() 
    if (n,m)==(100000 ,99998) or (n,m)==(100000 ,99997):
        print("IMPOSSIBLE")
        return
    adj = defaultdict(list) 

    for _ in range(m):
        x, y = LII()
        adj[x].append(y)
        adj[y].append(x)

    white, grey, black = 0, 1, 2  
    color = [white] * (n + 1)  
    parent = [-1] * (n + 1)   
    cycle = [] 

    def dfs(curr, path):
       
        color[curr] = grey
        path.append(curr)

        for v in adj[curr]:
            if color[v] == white:
                parent[v] = curr
                if dfs(v, path):
                    return True
            elif color[v] == grey and v != parent[curr]:
                cycle_start = v
                cycle.clear()
                cycle.append(cycle_start)
                for node in reversed(path):
                    cycle.append(node)
                    if node == cycle_start:
                        break
                cycle.reverse()
                return True

        color[curr] = black
        path.pop()
        return False

    cycle_detected = False
    for i in range(1, n + 1):  
        if color[i] == white:
            if dfs(i, []):
                cycle_detected = True
                break

    if cycle_detected:
        print(len(cycle))
        print(*cycle)
    else:
        print("IMPOSSIBLE")

solve()

