from collections import defaultdict
import sys
from bisect import *
def input(): return sys.stdin.readline().rstrip("\r\n")
inf = float('inf')
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    total = (n*(n + 1))//2
    for i in range(n):
        r = n - i 
        l = i + 1
        mul = total - l*r
        ans+=(a[i]==b[i])*(mul)
    # print(ans)
    d1 = defaultdict(list)
    d2 = defaultdict(list)
    d3 = defaultdict(list)
    p2 = defaultdict(lambda : [0])
    p3 = defaultdict(lambda : [0])
    for i,x in enumerate(b):
        d1[x].append(i)
        d2[x].append(i + 1)
        d3[x].append(-(n - i))
        p2[x].append(p2[x][-1] + i + 1)
        p3[x].append(p3[x][-1] + n - i)

    for i in range(n):
        # for j , l , r in d[a[i]]:
        #     if i > j:
        #         ans+=min(l,n-i)
        #     else:
        #         ans+=min(r,i + 1)
        j = bisect_right(d1[a[i]], i ) - 1
        #0...j min(i + 1,d2[j])
        # for k in range(j + 1):
        #     ans+=min(n  - i,d2[a[i]][k])
        if j>=0:
            k1 = bisect_right(d2[a[i]],n-i)
            k1 = min(k1,j + 1)
            # ans+=sum(d2[a[i]][:k1])
            ans+=p2[a[i]][k1] - p2[a[i]][0]
            if j>=k1:
                ans+=(n-i)*(j - k1 + 1)
        if j + 1 < len(d3[a[i]]): 
            k2 = bisect_right(d3[a[i]], -(i + 1), j + 1)  # Find split point
            
            ans += (i + 1) * (k2 - (j + 1))
            ans+=p3[a[i]][len(d3[a[i]])] - p3[a[i]][k2]
            # ans += sum(-x for x in d3[a[i]][k2:])
        # for k in range(j + 1,len(d3[a[i]])):
        #     ans+=min(i + 1,d3[a[i]][k])
    print(ans)
solve()