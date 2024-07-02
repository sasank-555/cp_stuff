from collections import defaultdict
import sys

sys.setrecursionlimit(200006)

N = int(input())
adj = defaultdict(list)
edges = list(map(int,input().split()))
for i,x in enumerate(edges):
  adj[x].append(i+2)
  adj[i+2].append(x)
dp = [0]*(N+1)
def dfs(i,p):
  dp[i] = 1
  for v in adj[i]:
    if v!=p:
      dfs(v,i)
      dp[i]+=dp[v]
dfs(1,0)
print(*([x-1 for x  in dp[1:]]))