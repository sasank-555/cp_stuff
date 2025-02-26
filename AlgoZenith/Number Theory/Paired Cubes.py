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
'''
Description: You are given n positive integers A1, A2, …, An. 
Your task is to find the number of pairs (i, j) such that the product Ai × Aj is a cube number (i.e., there exists an integer x for which x³ = Ai × Aj).
'''
def solve():
    n = II()
    nums = LII()
    mx = max(nums) + 1
    c = Counter()
    ans = 0
    SPF =   [i for i in range(mx)]
    for i in range(2,mx):
        if SPF[i] ==i:
            for j in range(i*i,mx,i):
                if SPF[j]==j:
                    SPF[j] = i
    for x in (nums):
        tar = 1
        norm = 1
        while x!=1:
            cnt = 0
            pf= SPF[x]
            while x%pf==0:
                cnt+=1
                x = x//pf
            cnt%=3
            for _ in range(cnt):
                norm*=pf
            for _ in range((3 - cnt)%3):
                tar*=pf
        ans+=c[tar]
        c[norm]+=1
    print(ans)

for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
