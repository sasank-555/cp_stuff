def solve(adj,n):
    LOG = 20
    par =[[0]*LOG for i in range(n + 1)]
    par[1][0] = 0
    dp = [0]*( n + 1)
    def dfs(u,p,dep):
        dp[u]  = dep
        par[u][0] = p
        for i in range(1,LOG + 1):
            if par[u][i-1]!=0:
                par[u][i] = par[par[u][i-1]][i-1] # remember this
        for v in adj[u]:
            if v!=p:
                dfs(v,u,dep + 1)
    dfs(1,0,0)
    def lca(u,v):
        if dp[u] < dp[v] : u,v = v,u
        for i in range(LOG - 1, -1 , -1):
            if ((dp[u] - dp[v])&(1<<i)): # u do a jump if the bit is on in its binary form
                u = par[u][i]
        if v==u:return v
        for i in range(LOG-1,-1,-1):
            if par[u][i]!=par[v][i]:
                u = par[u][i]
                v = par[v][i]
        return par[u][0]