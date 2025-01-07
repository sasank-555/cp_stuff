class SegmentTree:
    def __init__(self, nums, fn=min):
        self.n = len(nums)
        self.fn = fn
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, index, low, high):
        if low == high:
            self.tree[index] = nums[low]
        else:
            mid = (low + high) // 2
            self.build(nums, 2 * index + 1, low, mid)
            self.build(nums, 2 * index + 2, mid + 1, high)
            self.tree[index] = self.fn(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def rangeQuery_(self, index, low, high, left, right):
        if low >= left and high <= right:
            return self.tree[index]
        elif low > right or high < left:
            if self.fn == min:
                return float('inf')
            elif self.fn == max:
                return float('-inf')
            else:
                return 0
        else:
            mid = (low + high) // 2
            l = self.rangeQuery_(2 * index + 1, low, mid, left, right)
            r = self.rangeQuery_(2 * index + 2, mid + 1, high, left, right)
            return self.fn(l, r)

    def rangeQuery(self, left, right):
        return self.rangeQuery_(0, 0, self.n - 1, left, right)

    def update_(self, i, val, index, low, high):
        if low == high:
            self.tree[index] = val
            return
        mid = (low + high) // 2
        if i > mid:
            self.update_(i, val, 2 * index + 2, mid + 1, high)
        else:
            self.update_(i, val, 2 * index + 1, low, mid)
        self.tree[index] = self.fn(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def update(self, i, val):
        return self.update_(i, val, 0, 0, self.n - 1)
n,q = map(int,input().split())
arr=list(map(int,input().split()))
st = SegmentTree(arr)
for _ in range(q):
    l,r = map(lambda x : int(x) - 1,input().split())
    print(st.rangeQuery(l,r))
