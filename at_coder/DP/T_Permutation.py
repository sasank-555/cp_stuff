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
# 1 2 3 4 
#  < < >
#  <  
def solve():
    n = II()
    s = I()
    tg  = s.count(">")
    tl = s.count("<")
    def go(i,g):
        if i==n-1:
            return 1
        rg  = tg - g
        rl = tl - (i-g)
        a = 0
        b = 0
        if rg>0:
            a =go(i + 1, g + 1)
        if rl>0:
            b = go(i+ 1, g)
        return (a+b)%MOD1
    return go(0,0)

for _ in range(1):
    t  = solve()
    print(t)