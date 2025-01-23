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
def matmul(a,b):
    n = len(a)
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = sum(a[i][k]*b[k][j] for k in range(n))%MOD1
    return ans
def matpow(base,p):
    n = len(base)
    ans = [[0]*n for _ in range(n)]
    for i in range(n) : ans[i][i] = 1
    while p :
        if p & 1:
            ans = matmul(ans,base)
        base = matmul(base,base)
        p//=2
    return ans
def solve():
    n = II()
    t = [[0 , 1] , [1, 1]]
    ans = matpow(t,n)
    print(ans[0][1])
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")