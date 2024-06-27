# You are given a tree consisting of n nodes.
# A matching is a set of edges where each node is an endpoint of at most one edge. What is the maximum number of edges in a matching?
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
n  = int(input())
edges = [list(map(int,input().split())) for _ in range(n-1)]
adj = defaultdict(list)
for u,v in edges:
  adj[u-1].append(v-1)
  adj[v-1].append(u-1)
dp = [[0]*2 for _ in range(200005)]
def dfs(n,p):
  ans = - float('inf')
  for v in adj[n]:
    if v!=p:
      dfs(v,n)
      dp[n][0] += max(dp[v][1],dp[v][0])
  for v in adj[n]:
    if v!=p:
      dp[n][1] = max(dp[n][1],dp[v][0] + 1 + dp[n][0] - max(dp[v][1],dp[v][0]))
dfs(0,-1)
print(max(dp[0][1],dp[0][0]))
