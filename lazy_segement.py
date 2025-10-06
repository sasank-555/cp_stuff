import math

class SegTreeBeats:
    def __init__(self, arr):
        self.n = len(arr)
        N = 4 * self.n + 5
        self.sum = [0] * N

        # minima info
        self.mn = [math.inf] * N
        self.mn2 = [math.inf] * N
        self.cnt_mn = [0] * N

        # maxima info
        self.mx = [-math.inf] * N
        self.mx2 = [-math.inf] * N
        self.cnt_mx = [0] * N

        self.add = [0] * N

        if self.n > 0:
            self._build(0, 0, self.n - 1, arr)

    def _build(self, v, tl, tr, arr):
        if tl == tr:
            val = arr[tl]
            self.sum[v] = val
            self.mn[v] = val
            self.mn2[v] = math.inf
            self.cnt_mn[v] = 1
            self.mx[v] = val
            self.mx2[v] = -math.inf
            self.cnt_mx[v] = 1
            return
        tm = (tl + tr) // 2
        self._build(2*v+1, tl, tm, arr)
        self._build(2*v+2, tm+1, tr, arr)
        self._pull(v)

    def _pull(self, v):
        l, r = 2*v+1, 2*v+2
        self.sum[v] = self.sum[l] + self.sum[r]

        # combine maxima
        if self.mx[l] > self.mx[r]:
            self.mx[v] = self.mx[l]
            self.cnt_mx[v] = self.cnt_mx[l]
            self.mx2[v] = max(self.mx2[l], self.mx[r])
        elif self.mx[r] > self.mx[l]:
            self.mx[v] = self.mx[r]
            self.cnt_mx[v] = self.cnt_mx[r]
            self.mx2[v] = max(self.mx[l], self.mx2[r])
        else:
            self.mx[v] = self.mx[l]
            self.cnt_mx[v] = self.cnt_mx[l] + self.cnt_mx[r]
            self.mx2[v] = max(self.mx2[l], self.mx2[r])

        # combine minima
        if self.mn[l] < self.mn[r]:
            self.mn[v] = self.mn[l]
            self.cnt_mn[v] = self.cnt_mn[l]
            self.mn2[v] = min(self.mn2[l], self.mn[r])
        elif self.mn[r] < self.mn[l]:
            self.mn[v] = self.mn[r]
            self.cnt_mn[v] = self.cnt_mn[r]
            self.mn2[v] = min(self.mn[l], self.mn2[r])
        else:  # equal
            self.mn[v] = self.mn[l]
            self.cnt_mn[v] = self.cnt_mn[l] + self.cnt_mn[r]
            self.mn2[v] = min(self.mn2[l], self.mn2[r])

    def _apply_add(self, v, tl, tr, val):
        length = tr - tl + 1
        self.sum[v] += val * length

        self.mn[v] += val
        if self.mn2[v] != math.inf:
            self.mn2[v] += val

        self.mx[v] += val
        if self.mx2[v] != -math.inf:
            self.mx2[v] += val

        self.add[v] += val

    def _apply_chmin_node(self, v, x):
        # assume x < self.mx[v] and x > self.mx2[v]
        diff = x - self.mx[v]
        self.sum[v] += diff * self.cnt_mx[v]
        if self.mn[v] == self.mx[v]:
            self.mn[v] = x
        self.mx[v] = x

    def _apply_chmax_node(self, v, x):
        # assume x > self.mn[v] and x < self.mn2[v]
        diff = x - self.mn[v]
        self.sum[v] += diff * self.cnt_mn[v]
        if self.mx[v] == self.mn[v]:
            self.mx[v] = x
        self.mn[v] = x

    def _push(self, v, tl, tr):
        if tl == tr:
            return
        l, r = 2*v+1, 2*v+2
        tm = (tl + tr) // 2

        # push add
        if self.add[v] != 0:
            val = self.add[v]
            self._apply_add(l, tl, tm, val)
            self._apply_add(r, tm+1, tr, val)
            self.add[v] = 0

        # push chmin from parent to children if possible
        if self.mx[l] > self.mx[v]:
            if self.mx2[l] < self.mx[v]:
                self._apply_chmin_node(l, self.mx[v])
        if self.mx[r] > self.mx[v]:
            if self.mx2[r] < self.mx[v]:
                self._apply_chmin_node(r, self.mx[v])

        # push chmax from parent to children if possible
        if self.mn[l] < self.mn[v]:
            if self.mn2[l] > self.mn[v]:
                self._apply_chmax_node(l, self.mn[v])
        if self.mn[r] < self.mn[v]:
            if self.mn2[r] > self.mn[v]:
                self._apply_chmax_node(r, self.mn[v])

    def _range_add(self, v, tl, tr, l, r, val):
        if l > r:
            return
        if tl == l and tr == r:
            self._apply_add(v, tl, tr, val)
            return
        self._push(v, tl, tr)
        tm = (tl + tr) // 2
        self._range_add(2*v+1, tl, tm, l, min(r, tm), val)
        self._range_add(2*v+2, tm+1, tr, max(l, tm+1), r, val)
        self._pull(v)

    def _range_chmin(self, v, tl, tr, l, r, x):
        if l > r or x >= self.mx[v]:
            return
        if tl == l and tr == r and x > self.mx2[v]:
            self._apply_chmin_node(v, x)
            return
        self._push(v, tl, tr)
        tm = (tl + tr) // 2
        self._range_chmin(2*v+1, tl, tm, l, min(r, tm), x)
        self._range_chmin(2*v+2, tm+1, tr, max(l, tm+1), r, x)
        self._pull(v)

    def _range_chmax(self, v, tl, tr, l, r, x):
        if l > r or x <= self.mn[v]:
            return
        if tl == l and tr == r and x < self.mn2[v]:
            self._apply_chmax_node(v, x)
            return
        self._push(v, tl, tr)
        tm = (tl + tr) // 2
        self._range_chmax(2*v+1, tl, tm, l, min(r, tm), x)
        self._range_chmax(2*v+2, tm+1, tr, max(l, tm+1), r, x)
        self._pull(v)

    def range_add(self, l, r, val):
        if l < 0: l = 0
        if r >= self.n: r = self.n-1
        if l > r or self.n == 0: return
        self._range_add(0, 0, self.n-1, l, r, val)

    def range_chmin(self, l, r, x):
        if l < 0: l = 0
        if r >= self.n: r = self.n-1
        if l > r or self.n == 0: return
        self._range_chmin(0, 0, self.n-1, l, r, x)

    def range_chmax(self, l, r, x):
        if l < 0: l = 0
        if r >= self.n: r = self.n-1
        if l > r or self.n == 0: return
        self._range_chmax(0, 0, self.n-1, l, r, x)

    def _query_sum(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if tl == l and tr == r:
            return self.sum[v]
        self._push(v, tl, tr)
        tm = (tl + tr) // 2
        return self._query_sum(2*v+1, tl, tm, l, min(r, tm)) + \
               self._query_sum(2*v+2, tm+1, tr, max(l, tm+1), r)

    def query_sum(self, l, r):
        if l < 0: l = 0
        if r >= self.n: r = self.n-1
        if l > r or self.n == 0: return 0
        return self._query_sum(0, 0, self.n-1, l, r)

    def _query_max(self, v, tl, tr, l, r):
        if l > r:
            return -math.inf
        if tl == l and tr == r:
            return self.mx[v]
        self._push(v, tl, tr)
        tm = (tl + tr) // 2
        return max(self._query_max(2*v+1, tl, tm, l, min(r, tm)),
                   self._query_max(2*v+2, tm+1, tr, max(l, tm+1), r))

    def query_max(self, l, r):
        if l < 0: l = 0
        if r >= self.n: r = self.n-1
        if l > r or self.n == 0: return -math.inf
        return self._query_max(0, 0, self.n-1, l, r)

    def _query_min(self, v, tl, tr, l, r):
        if l > r:
            return math.inf
        if tl == l and tr == r:
            return self.mn[v]
        self._push(v, tl, tr)
        tm = (tl + tr) // 2
        return min(self._query_min(2*v+1, tl, tm, l, min(r, tm)),
                   self._query_min(2*v+2, tm+1, tr, max(l, tm+1), r))

    def query_min(self, l, r):
        if l < 0: l = 0
        if r >= self.n: r = self.n-1
        if l > r or self.n == 0: return math.inf
        return self._query_min(0, 0, self.n-1, l, r)