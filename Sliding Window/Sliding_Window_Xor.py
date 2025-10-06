n , k = map(int,input().split())
x,a,b,c = map(int,input().split())
prev = x
s = x
import collections
q = collections.deque([x])
for _ in range(k - 1):
    element = (a * q[-1] + b)%c
    s^=element
    q.append(element)
ans = s
for _ in range(k,n):
    element = (a * q[-1]  + b)%c
    s^=q.popleft()
    s^=element
    q.append(element)
    ans = ans ^ s
print(ans)
