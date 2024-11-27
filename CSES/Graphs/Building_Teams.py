from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    
    adj = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    
    color = [-1] * (n + 1)
    

    def bfs(start):
        queue = deque([start])
        color[start] = 0  
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1: 
                    color[neighbor] = 1 - color[node]  
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  
                    return False
        return True
    
    
    for i in range(1, n + 1):
        if color[i] == -1:  
            if not bfs(i):  
                print("IMPOSSIBLE")
                return
    

    result = []
    for i in range(1, n + 1):
        
        result.append(str(color[i] + 1)) 
    
    
    print(" ".join(result))


solve()
