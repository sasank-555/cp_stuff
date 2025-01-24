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
dirs = [[0,1],[1,0],[-1,0],[0,-1]]
def solve():
    n,m= LII()
    grid =[I() for _ in range(n)]
    q = deque()
    dis = [[inf]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="M":
                q.append((i,j, 0))
                dis[i][j] = 0
    while q:
        x, y , d = q.popleft() 
        for dx,dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and 1 + d < dis[nx][ny] and grid[nx][ny]!="#":
                dis[nx][ny] = 1 + d
                q.append((nx,ny,1 + d))
    # for x in dis:print(*x)
    q = deque()
    vis = set()
    curri = None
    currj = None
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="A":
                q.append((0,i,j,-1,-1))
                vis.add((i,j))
                break
    par = {}
    while q:
        d , i, j , pi,pj = q.popleft()
        # print(i,j)
        par[(i,j)] = (pi,pj)
        if  i==0 or i==n-1 or j==0 or j==m-1:
            curri = i
            currj = j
            break
        
        for dx,dy in dirs:
            nx = i  + dx
            ny = j  + dy
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in vis and 1 + d < dis[nx][ny] and grid[nx][ny]!="#":
                # print("here")
                q.append((1 + d,nx,ny,i,j))
                vis.add((nx,ny))
    if curri==None:
        print("NO")
        return
    print("YES")
    def l(i,j,pi,pj):
        if i==pi + 1:return "D"
        if j==pj + 1:return "R"
        if i==pi - 1:return "U"
        if j==pj - 1:return "L"
    ans = []
    while True:
        pi,pj = par[(curri,currj)]
        # print(curri,currj,pi,pj)
        if pi==-1:break
        ans.append(l(curri,currj,pi,pj))
        curri, currj = pi,pj
    print(len(ans))
    print("".join(ans[::-1]))
for _ in range(1):
    t  = solve()
    #print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")
