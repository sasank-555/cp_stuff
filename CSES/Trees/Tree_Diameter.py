from collections import defaultdict, deque
import sys
sys.setrecursionlimit(200006)
# if A,B are the end points of diamters then for any arbitary node the farthest node will be either A or B
N = int(input())
adj = defaultdict(list)
for _ in range(N-1):
  x,y  = map(int,input().split())
  adj[x].append(y)
  adj[y].append(x)
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
fnode , _  = bfs(1)
_ , diameter = bfs(fnode)
print(diameter)
