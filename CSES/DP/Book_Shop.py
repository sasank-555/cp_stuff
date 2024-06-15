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
n,x = LII()
prices = LII()
pages =LII()
def max_pages(n, x):
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(x + 1):            
            dp[i][j] = dp[i-1][j]
            if j >= prices[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-prices[i-1]] + pages[i-1])
    return dp[n][x]

print(max_pages(0,0))