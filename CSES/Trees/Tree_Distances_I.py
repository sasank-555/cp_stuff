from collections import defaultdict, deque
import sys
# if A,B are the end points of diamters then for any arbitary node the farthest node will be either A or B
sys.setrecursionlimit(200006)
N = int(input())
adj = defaultdict(list)
for _ in range(N-1):
  x,y  = map(int,input().split())
  adj[x].append(y)
  adj[y].append(x)
dp = [0]*(N+1)
def bfs(node):
  q = deque()
  q.append((node,0))
  vis = set([node])
  max_dis= 0
  max_node = node
  while q:
    i,d = q.popleft()
    if d>max_dis:
      max_dis = d
      max_node = i
    for v in adj[i]:
      if v not in vis:
        vis.add(v)
        q.append((v,d+1))
  return (max_node,max_dis)
a,_ = bfs(1)
b,_ = bfs(a)

q = deque()
q.append((a,0))
vis = set()
vis.add(a)
while q:
  i,d = q.popleft()
  dp[i] = max(dp[i] , d)
  for v in adj[i]:
    if v not in vis:
      vis.add(v)
      q.append((v,d+1))
q.clear()
vis.clear()
q.append((b,0))
vis.add(b)
while q:
  i,d = q.popleft()
  dp[i] = max(dp[i] , d)
  for v in adj[i]:
    if v not in vis:
      vis.add(v)
      q.append((v,d+1))

print(*(dp[1:]))