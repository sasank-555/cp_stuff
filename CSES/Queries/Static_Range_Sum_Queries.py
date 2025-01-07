from sys import stdin
def input() : return stdin.readline().rstrip("\r\n")
n,q = map(int,input().split())
arr = list(map(int,input().split()))
p =[0]
for i in range(n):
    p.append(p[-1] + arr[i])
for _ in range(q):
    a,b = map(int,input().split())
    print(p[b] - p[a-1])
