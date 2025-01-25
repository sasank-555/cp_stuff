import sys
def input(): return sys.stdin.readline().rstrip("\r\n")
from collections import defaultdict
inf = float('inf')
def solve():
    n = int(input())
    f = [0]*(n + 1)
    nums = list(map(int, input().split()))
    # x,y,z 
    # 1  8 8 
    # 2 8 8
    # 3 8  8
    # 
    s  = 0 
    ans = 0
    d = defaultdict(list)  
    for i,x in enumerate(nums):
        d[x].append(i)
    p = [0]*(n)
    nst = set()
    for i in range(n):
        nst.add(nums[i])
        p[i] = len(nst)
    # print(p)
    for x in d:
        if len(d[x])>=2:
            i , j = d[x][-2] , d[x][-1]
            if i-1>=0:
                ans+=p[i-1]
                if len(d[x])>=3:
                    ans-=1
    print(ans)
    # st = set()
    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             if i < j and j < k and nums[i]!=nums[j] and nums[j]==nums[k]:
    #                 st.add((nums[i],nums[j],nums[k]))
    # print(st)
    # print(len(st))                  
    
    # for i in range(n-1,-1,-1):
    #     s-=(f[nums[i]]>=2)
    #     ans+=s
    #     f[nums[i]]+=1
    #     s+=(f[nums[i]]>=2)
    #     # ss+=f[nums[i]]**2
    # print(ans)

solve()