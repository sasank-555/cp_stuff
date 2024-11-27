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
    parent = list(range(n+1))
    rank = [0]*(n+1)
    def find(x):
        if x==parent[x]:
            return x 
        parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        ux , uy = find(x),find(y)
        if ux==uy:
            return 
        if rank[ux] > rank[uy]:
            parent[uy] = ux
        elif rank[ux] < rank[uy] : parent[ux] = uy
        else:
            parent[uy] = ux
            rank[ux]+=1
    for _ in range(m):
        x,y = LII()
        union(x,y)
    up = [i for i in range(1,n + 1) if i==find(i)]
    print(len(up)-1)
    for i in range(1,len(up)):
        print(up[i],up[i-1])
solve()