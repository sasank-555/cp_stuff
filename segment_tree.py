class node:
    def __init__(self):
        self.sum = 0
        self.mx = -float('inf')
        self.mi = float('inf')

def combine(n1, n2, ret):
    ret.sum = n1.sum + n2.sum
    ret.mx = max(n1.mx, n2.mx)
    ret.mi = min(n1.mi, n2.mi)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [node() for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1)

    def build(self, v, tl, tr):
        if tl == tr:
            val = self.data[tl]
            self.tree[v].sum = val
            self.tree[v].mx = val
            self.tree[v].mi = val
            return
        tm = (tl + tr) // 2
        self.build(2*v + 1, tl, tm)
        self.build(2*v + 2, tm + 1, tr)
        combine(self.tree[2*v + 1], self.tree[2*v + 2], self.tree[v])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return node()
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left = self.query(2*v + 1, tl, tm, l, min(r, tm))
        right = self.query(2*v + 2, tm + 1, tr, max(l, tm + 1), r)
        res = node()
        combine(left, right, res)
        return res

    def update(self, v, tl, tr, pos, val):
        if tl == tr:
            self.tree[v].sum = val
            self.tree[v].mx = val
            self.tree[v].mi = val
            return
        tm = (tl + tr) // 2
        if pos <= tm:
            self.update(2*v + 1, tl, tm, pos, val)
        else:
            self.update(2*v + 2, tm + 1, tr, pos, val)
        combine(self.tree[2*v + 1], self.tree[2*v + 2], self.tree[v])

    def range_query(self, l, r):
        return self.query(0, 0, self.n - 1, l, r)

    def point_update(self, pos, val):
        self.update(0, 0, self.n - 1, pos, val)
