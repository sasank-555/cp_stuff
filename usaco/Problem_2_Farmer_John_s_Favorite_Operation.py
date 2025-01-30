import sys
def input(): return sys.stdin.readline().rstrip("\r\n")
inf = float('inf')
def solve():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    inf = float('inf')
    best = inf
    r = [x % m for x in a]
    r.sort()
    p = [0]
    for x in r:
        p.append(p[-1] + x)
    for i in range(n):
        curr = 0
        l = i
        rr = n - 1
        temp = l
        while l <= rr:
            mid = (l + rr) // 2
            if r[mid] - r[i] <= m + r[i] - r[mid]:
                temp = mid
                l = mid + 1
            else:
                rr = mid -1
        curr += p[temp + 1] - p[i] - (temp - i + 1) * r[i]
        curr += (r[i] + m) * (n - (temp + 1)) - (p[n] - p[temp + 1])
        l = 0
        rr = i
        temp2 = i
        while l <= rr:
            mid = (l + rr) // 2
            if r[i] - r[mid] <= m - (r[i] - r[mid]):
                rr = mid - 1
                temp2 = mid
            else:
                l = mid + 1
        curr += (i + 1 - temp2) * r[i] - (p[i + 1] - p[temp2])
        curr += (m - r[i]) * temp2 + p[temp2]
        best = min(best, curr)
    print(best)


for _ in range(int(input())):
    solve()
