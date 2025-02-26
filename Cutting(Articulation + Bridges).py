N = 200000
timer = 0
vis = set()
tin = [0] * N
low = [0] * N
cut_points = set()
bridges = []  # renamed to bridges (plural) for clarity
adj = [[] for _ in range(N)]

def dfs(u, parent=-1):
    global timer
    vis.add(u)
    children = 0
    tin[u] = low[u] = timer
    timer += 1
    for v in adj[u]:
        if v == parent:
            continue
        if v in vis:
            # back edge.
            low[u] = min(low[u], tin[v])
        else:
            dfs(v, u)
            low[u] = min(low[u], low[v])
            # If u is not the root and the condition holds, u is an articulation point.
            if parent != -1 and low[v] >= tin[u]:
                cut_points.add(u)
            # (u, v) is a bridge if no back edge from v (or its descendants) reaches above u.
            if low[v] > tin[u]:
                bridges.append((u, v))
            children += 1
    # Special case for root: it is an articulation point if it has more than one child.
    if parent == -1 and children > 1:
        cut_points.add(u)
