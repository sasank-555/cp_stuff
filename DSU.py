class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)
        self.size = [1] * (n+1)

    def find(self, x):
        # Time Complexity: O(α(n)), where α is the Inverse Ackermann function
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Time Complexity: O(α(n)), where α is the Inverse Ackermann function
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]

    def connected(self, x, y):
        # Time Complexity: O(α(n)), where α is the Inverse Ackermann function
        return self.find(x) == self.find(y)

    def get_size(self, x):
        # Time Complexity: O(α(n)), where α is the Inverse Ackermann function
        root = self.find(x)
        return self.size[root]
