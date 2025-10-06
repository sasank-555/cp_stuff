# 3 forms
# In-Out DP
# Knapsack
# Parent , Ancestral Property


# IN OUT DP
# You are given a tree consisting of n nodes.
# Your task is to determine for each node the maximum distance to another node.
from math import inf
def solve(n,adj):
    indp = [0]*n
    outdp = [0]*n
    def go(u,p):
        indp[u] = 0
        for v in adj[u]:
            if v==p:continue
            go(v,u)
            indp[u] = max(1 + indp[v] , indp[u])
    go(0,-1)
    def goout(u,p,outVal):
        outdp[u] = outVal
        a , b  = -inf,-inf
        for v in adj[u]:
            if v==p:continue
            if indp[v] > a:
                a,b = indp[v],a
            if indp[v] > b:
                b = indp[v]
        for  v in adj[u]:
            if v==p:
                continue
            outvalforchild = max(2 + a if indp[v]!=a else b, 1 + outdp[u])
            goout(v,u,outvalforchild)
    goout(0,-1,0)
    ans = [max(x,y) for x,y in zip(indp,outdp)]

    # knapsack style
    # each node has val , choose exactly k nodes no two should be neighbour ,so such that sum of choosen nodes is maximum
    def solve(adj,n,nums,k):
        def go(u,p,f):
            # pick this
            if f==1: 
                ret = [-inf]*(k+1)
                ret[1] = nums[u]
                for v in adj[u]:
                    if v==p:
                        continue
                    chid = go(v,u,0)
                    for a in range(k,-1,-1):
                        for b in range(k,-1,-1):
                            ret[a + b] = max(ret[a + b],ret[a] + chid[b])
                    return ret
            else:
                ret = [-inf]*(k+1)
                ret[0] = 0
                for v in adj[u]:
                    if v==p:
                        continue
                    chiddontpick = go(v,u,0)
                    chidpick = go(v,u,1)
                    for a in range(k,-1,-1):
                        for b in range(k,-1,-1):
                            ret[a + b] = max(ret[a + b],ret[a] + max(chidpick[b],chiddontpick[b]))
                    return ret
        return max(go(0,-1,0)[-1],go(0,-1,1)[-1])



