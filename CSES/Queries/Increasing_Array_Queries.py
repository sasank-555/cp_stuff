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
    n,q = LII()
    nums = LII()
    n = len(nums)
    LOG = n.bit_length() + 1
    nge = [n]*n
    p =[0]
    st = []
    for i in range(n - 1,-1,-1):
        while st and nums[st[-1]]<=nums[i]:
            st.pop()
        if st:
            nge[i] = st[-1]
        st.append(i)
    parent =[[n]*LOG for _ in range(n + 1)]
    ops = [[0]*LOG for _ in range(n + 1)]
    for i in  range(n):
        p.append(p[-1] + nums[i])
        ops[i][0] = nums[i]*(nge[i] - i)
        parent[i][0] = nge[i]
    for l in range(1,LOG):
        for i in  range(n):
            ops[i][l] = ops[i][l-1] + ops[parent[i][l-1]][l-1]
            parent[i][l] = parent[parent[i][l-1]][l-1]
    for _ in range(q):
        l,r = LGLII()
        curr = l
        cost = 0
        for ll in range(LOG-1,-1,-1):
            if parent[curr][ll]<=r:
                cost+=ops[curr][ll]
                curr = parent[curr][ll]
        cost+=(r-curr+1)*(nums[curr])
        cost-=(p[r+1] - p[l])
        print(cost)            

for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
