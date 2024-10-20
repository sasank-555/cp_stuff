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
from math import gcd
def lcm(a,b):
  return a*b//gcd(a,b)
N  = II()
nums = LII()
mx = max(nums)
sieve = [1]*(mx+1)
sieve[1]=sieve[0] = 0
d = [[] for _ in range(mx+1)]
e = Counter(nums)
for i in range(2,mx+1):
  if len(d[i])==0:
    d[i].append(i)
    for j in range(2*i,mx+1,i):
      d[j].append(i)
factors = [0]*(mx + 1)
primeDivisors = [0]*(mx + 1)
for x in nums:
  for i in range(1,1<<(len(d[x]))):
    combination = 1
    no = 0
    for j in range(len(d[x])):
      if i & (1<<j):
        combination*= d[x][j]
        no+=1
    factors[combination]+=1
    primeDivisors[combination] = no
tot = (N*(N-1))//2
ans = 0
for i in range(mx+1):
  if primeDivisors[i]& 1:
    ans+= (factors[i]*(factors[i]-1))//2
  else:
    ans-= (factors[i]*(factors[i]-1))//2
print(tot-ans)


