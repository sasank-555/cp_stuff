class Classic:
    def __init__(self, n, adj):
        self.n = n
        self.LOG = n.bit_length()
        self.adj = adj
        self.par = [[0] * self.LOG for _ in range(n)]
        self.lvl = [0] * n
        stack = [(0, 0)]
        while stack:
            u, depth = stack.pop()
            self.lvl[u] = depth
            for v in self.adj[u]:
                if v != self.par[u][0]:
                    self.par[v][0] = u
                    stack.append((v, depth + 1))
        for j in range(1, self.LOG):
            for u in range(n):
                self.par[u][j] = self.par[self.par[u][j - 1]][j - 1]
    def lca(self, u, v):
        if self.lvl[u] < self.lvl[v]:
            u, v = v, u
        diff = self.lvl[u] - self.lvl[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                u = self.par[u][i]
        if u == v:
            return u
        for i in reversed(range(self.LOG)):
            if self.par[u][i] != self.par[v][i]:
                u = self.par[u][i]
                v = self.par[v][i]
        return self.par[u][0]
    def normaldist(self, u, v):
        return self.lvl[u] + self.lvl[v] - 2 * self.lvl[self.lca(u, v)]

    def kthAncestor(self,u,k):
        for i in range(self.LOG-1,-1,-1):
            if k&(1<<i):
                u = self.par[u][i]
        return u
class PathAggregateWithNodeVal:
    def __init__(self, n, adj, val, f=lambda x, y: x + y):
        self.n = n
        self.adj = adj
        self.val = val[:]            
        self.f = f
        self.LOG = n.bit_length() + 1
        self.par = [[0] * self.LOG for _ in range(n)]
        self.dp  = [[0] * self.LOG for _ in range(n)]
        self.lvl = [0] * n
        stack = [(0, 0)]
        while stack:
            u, depth = stack.pop()
            self.lvl[u] = depth
            self.dp[u][0] = self.val[u]
            for v in self.adj[u]:
                if v != self.par[u][0]:
                    self.par[v][0] = u
                    stack.append((v, depth + 1))
        for j in range(1, self.LOG):
            for u in range(n):
                pu = self.par[u][j - 1]
                self.par[u][j] = self.par[pu][j - 1]
                self.dp[u][j] = self.f(self.dp[u][j - 1], self.dp[pu][j - 1])

    def lca(self, u, v):
        if self.lvl[u] < self.lvl[v]:
            u, v = v, u
        diff = self.lvl[u] - self.lvl[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                u = self.par[u][i]
        if u == v:
            return u
        for i in reversed(range(self.LOG)):
            if self.par[u][i] != self.par[v][i]:
                u = self.par[u][i]
                v = self.par[v][i]
        return self.par[u][0]

    def normaldist(self, u, v):
        return self.lvl[u] + self.lvl[v] - 2 * self.lvl[self.lca(u, v)]

    def query(self, u, v):
        if self.lvl[u] < self.lvl[v]:
            u, v = v, u
        ans = None
        diff = self.lvl[u] - self.lvl[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                ans = self.dp[u][i] if ans is None else self.f(ans, self.dp[u][i])
                u = self.par[u][i]
        if u == v:
            return self.f(ans, self.val[u]) if ans is not None else self.val[u]
        for i in reversed(range(self.LOG)):
            if self.par[u][i] != self.par[v][i]:
                ans = self.f(ans, self.dp[u][i])
                ans = self.f(ans, self.dp[v][i])
                u = self.par[u][i]
                v = self.par[v][i]
        ans = self.f(ans, self.val[u])
        ans = self.f(ans, self.val[v])
        return self.f(ans, self.val[self.par[u][0]])
    def kthAncestor(self,u,k):
        for i in range(self.LOG-1,-1,-1):
            if k&(1<<i):
                u = self.par[u][i]
        return u
class PathAggregateWithEdgeWeight:
    def __init__(self, n, adj, f=lambda x, y: x + y, identity=0):
        self.n = n
        self.adj = adj
        self.f = f
        self.identity = identity
        self.LOG = n.bit_length() + 1
        self.par = [[0] * self.LOG for _ in range(n)]
        self.dp  = [[identity] * self.LOG for _ in range(n)]
        self.lvl = [0] * n

        stack = [(0, 0)]
        while stack:
            u, depth = stack.pop()
            self.lvl[u] = depth
            for v, w in self.adj[u]:
                if v != self.par[u][0]:
                    self.par[v][0] = u
                    self.dp[v][0]  = w       
                    stack.append((v, depth + 1))

        for j in range(1, self.LOG):
            for u in range(n):
                pu = self.par[u][j - 1]
                self.par[u][j] = self.par[pu][j - 1]
                self.dp[u][j] = self.f(self.dp[u][j - 1],
                                       self.dp[pu][j - 1])

    def lca(self, u, v):
        if self.lvl[u] < self.lvl[v]:
            u, v = v, u
        diff = self.lvl[u] - self.lvl[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                u = self.par[u][i]

        if u == v:
            return u

        for i in reversed(range(self.LOG)):
            if self.par[u][i] != self.par[v][i]:
                u = self.par[u][i]
                v = self.par[v][i]

        return self.par[u][0]

    def normaldist(self, u, v):
        return self.lvl[u] + self.lvl[v] - 2 * self.lvl[self.lca(u, v)]

    def query(self, u, v):
        """
        Aggregate f(edge‐weights) over the unique path u↔v.
        """
        if self.lvl[u] < self.lvl[v]:
            u, v = v, u

        ans = self.identity
        diff = self.lvl[u] - self.lvl[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                ans = self.f(ans, self.dp[u][i])
                u = self.par[u][i]
        if u == v:
            return ans

        for i in reversed(range(self.LOG)):
            if self.par[u][i] != self.par[v][i]:
                ans = self.f(ans, self.dp[u][i])
                ans = self.f(ans, self.dp[v][i])
                u = self.par[u][i]
                v = self.par[v][i]
        ans = self.f(ans, self.dp[u][0])
        ans = self.f(ans, self.dp[v][0])
        return ans
    def kthAncestor(self,u,k):
        for i in range(self.LOG-1,-1,-1):
            if k&(1<<i):
                u = self.par[u][i]
        return u