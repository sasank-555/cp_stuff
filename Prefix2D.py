class PreFixSumMatrix:
    def __init__(self, mat, t=lambda x, y: x + y, neutral=0):
        """
        Initializes the prefix matrix with a custom operation.
        
        Args:
            mat (list of list of int/float): Input matrix.
            t (callable): A lambda function defining the operation (e.g., addition, multiplication).
            neutral (int/float): Neutral element for the operation (e.g., 0 for addition, 1 for multiplication).
        """
        self.mat = mat
        self.t = t
        self.neutral = neutral
        self.m, self.n = len(mat), len(mat[0])
        self.pre = [[neutral] * (self.n + 1) for _ in range(self.m + 1)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.pre[i + 1][j + 1] = t(
                    t(self.pre[i][j + 1], self.pre[i + 1][j]),
                    -self.pre[i][j]
                )
                self.pre[i + 1][j + 1] = t(self.pre[i + 1][j + 1], mat[i][j])
    
    def query(self, xa: int, ya: int, xb: int, yb: int) -> int:
        """Query the custom operation over the submatrix defined by top-left (xa, ya) and bottom-right (xb, yb)."""
        assert 0 <= xa <= xb < self.m
        assert 0 <= ya <= yb < self.n
        return self.t(
            self.t(self.pre[xb + 1][yb + 1], -self.pre[xb + 1][ya]),
            -self.t(self.pre[xa][yb + 1], self.pre[xa][ya])
        )
