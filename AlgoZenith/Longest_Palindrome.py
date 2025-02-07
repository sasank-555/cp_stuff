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
    s = I()
    n = len(s)
    h = [0]
    mod = random.getrandbits(64)
    pp = [1]
    p = random.randint(150,2*150)
    for x in s:
        h.append((h[-1]*p + ord(x))%mod)
        pp.append((pp[-1]*p)%mod)
    rh = [0]
    rpp = [1]
    for  x in s[::-1]:
        rh.append((rh[-1]*p + ord(x))%mod)
        rpp.append((rpp[-1] *p)%mod)
    def ok(l,r):
        h1  = (h[r + 1] - h[l]*pp[r - l + 1])%mod 
        r , l = n  - l  -1 , n - r  - 1
        h2 =  (rh[r + 1] - rh[l]*rpp[r - l + 1])%mod
        return h1==h2
    mx  = 1
    for i in range(n):
        l = 0
        r  = min(n-i-1, i)
        got = 0
        while l<=r:
            mid = (l + r)//2
            if ok(i - mid,i + mid):
                got = mid
                l = mid + 1
            else: r = mid - 1
        mx = max(mx,2*got + 1)
    for i in range(n-1):
        if s[i]!=s[i + 1]:continue
        l = 0
        got = 0
        r = min(i,n - i - 2)
        while l<=r:
            mid = (l + r)//2
            if ok(i-mid,i + mid + 1):
                got  = mid
                l = mid + 1
            else:
                r = mid - 1
        mx = max(mx,2*got + 2)
    for i in range(n):
        if i + mx-1>=n:break
        if ok(i,i + mx - 1):
            print(s[i : i + mx])
            break
        
for _ in range(II()):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
