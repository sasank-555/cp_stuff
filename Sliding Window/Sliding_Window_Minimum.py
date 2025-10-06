n , k = map(int,input().split())
x,a,b,c = map(int,input().split())
prev = x
s = x
import collections
q = collections.deque()
ans = 0
nums=[]
for i in range(n):
    element = ((a * nums[-1] + b)%c if i > 0 else x)
    while q and q[-1] > element:
        q.pop()
    q.append(element)
    if i>=k and q[0]==nums[i-k]:
        q.popleft()
    if i>=k-1:
        ans = ans^q[0]
    nums.append(element)
print(ans)