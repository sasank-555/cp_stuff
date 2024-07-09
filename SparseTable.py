class SparseTable:
    def __init__(self, data, fn=min):
        """
        Initialize the Sparse Table with the given data array and function.
        
        :param data: List[int] - The input array for which the Sparse Table is to be constructed.
        :param fn: function - The function to be used for range queries (e.g., min, max, gcd).
        """
        self.n = len(data)
        self.data = data
        self.fn = fn
        
        # Precompute log values
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        self.k = self.log[self.n] + 1
        self.st = [[0] * self.k for _ in range(self.n)]
        
        self._build()

    def _build(self):
        """
        Build the Sparse Table using the given function.
        """
        for i in range(self.n):
            self.st[i][0] = self.data[i]

        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[i][j] = self.fn(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, l, r):
        """
        Query the function value in the range [l, r].
        
        :param l: int - Left index of the range (inclusive).
        :param r: int - Right index of the range (inclusive).
        :return: int - The function value in the range [l, r].
        """
        j = self.log[r - l + 1]
        return self.fn(self.st[l][j], self.st[r - (1 << j) + 1][j])