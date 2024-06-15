class SegmentTree:
    def __init__(self, nums):
        """
        Constructor to initialize the segment tree.
        
        Time Complexity: O(N)
        """
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)  # Lazy array for lazy propagation
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, index, low, high):
        """
        Builds the segment tree recursively.
        
        Time Complexity: O(N)
        """
        if low == high:
            self.tree[index] = nums[low]
        else:
            mid = (low + high) // 2
            self.build(nums, 2 * index + 1, low, mid)
            self.build(nums, 2 * index + 2, mid + 1, high)
            self.tree[index] = min(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def range_query(self, left, right):
        """
        Performs a range query (finds the minimum value within a given range).
        
        Time Complexity: O(log N)
        """
        return self.range_query_util(0, 0, self.n - 1, left, right)

    def range_query_util(self, index, low, high, left, right):
        """
        Utility function for range query.
        
        Time Complexity: O(log N)
        """
        if self.lazy[index] != 0:
            self.tree[index] += self.lazy[index]
            if low != high:
                self.lazy[2 * index + 1] += self.lazy[index]
                self.lazy[2 * index + 2] += self.lazy[index]
            self.lazy[index] = 0

        if low >= left and high <= right:
            return self.tree[index]
        elif low > right or high < left:
            return float('inf')
        else:
            mid = (low + high) // 2
            l = self.range_query_util(2 * index + 1, low, mid, left, right)
            r = self.range_query_util(2 * index + 2, mid + 1, high, left, right)
            return min(l, r)

    def update_range(self, left, right, delta):
        """
        Updates a range of elements with a given delta value.
        
        Time Complexity: O(log N)
        """
        self.update_range_util(0, 0, self.n - 1, left, right, delta)

    def update_range_util(self, index, low, high, left, right, delta):
        """
        Utility function for updating range with lazy propagation.
        
        Time Complexity: O(log N)
        """
        if self.lazy[index] != 0:
            self.tree[index] += self.lazy[index]
            if low != high:
                self.lazy[2 * index + 1] += self.lazy[index]
                self.lazy[2 * index + 2] += self.lazy[index]
            self.lazy[index] = 0

        if low > right or high < left:
            return

        if low >= left and high <= right:
            self.tree[index] += delta
            if low != high:
                self.lazy[2 * index + 1] += delta
                self.lazy[2 * index + 2] += delta
            return

        mid = (low + high) // 2
        self.update_range_util(2 * index + 1, low, mid, left, right, delta)
        self.update_range_util(2 * index + 2, mid + 1, high, left, right, delta)
        self.tree[index] = min(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def update(self, i, val):
        """
        Updates a single element at index i with the given value.
        
        Time Complexity: O(log N)
        """
        delta = val - self.query(i, i)
        self.update_range(i, i, delta)
