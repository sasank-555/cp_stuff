import sys
def input(): return sys.stdin.readline().rstrip("\r\n")
inf = float('inf')
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pt = [[0] for _ in range(n)]
    re = a[::-1]
    for i in range(n):
        for j in range(n):
            pt[i].append(pt[i][-1] + (re[j]==b[j]))
        re = re[1:] + [re[0]]
    def lefty(i,j):
        return (j - i + n)%n
    ans = [0]*(n + 1)
    p = [0]
    for i in range(n):
        p.append(p[-1] + (a[i]==b[i]))
    tot = p[-1]
    for l in range(n):
        for r in range(l,n):
            delta = lefty(l,n - r - 1)
            uff = pt[delta][r + 1] - pt[delta][l] + tot - (p[r + 1] -p[l])
            ans[uff]+=1
    for  x in ans:print(x)

            
solve()