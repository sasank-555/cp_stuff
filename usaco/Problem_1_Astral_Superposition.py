import sys
def input(): return sys.stdin.readline().rstrip("\r\n")
def solve():
    # b  both 
    # w empty
    # g one
    n,a,b = list(map(int,input().split()))
    grid = [list(input()) for _ in range(n)]
    if a==0 and b==0:
        cnt = 0
        for x in grid:
            for v in x:
                cnt+=(v=="B" or v=="G")
        return cnt
    ans  = 0 
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='B':
                if 0<=i-b<n and 0<=j-a<n:
                    ni = i - b
                    nj = j - a
                    if grid[ni][nj]=="W": return -1
                    elif grid[ni][nj]=="G":
                        ans+=1
                        grid[ni][nj]="W"
                        grid[i][j] = "G"
                    else:
                        return -1
                else:
                    return -1
    # print(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='G':
                if 0<=i+b<n and 0<=j+a<n and grid[i+b][j+a]=='G':
                    grid[i][j]='L'
                    grid[i+b][j+a]='L'
                    ans+=1
                else :
                    ans+=1
                    grid[i][j]="L"
    # print(grid)
    return ans


'''
GWGWW
WGWWW
WBWGW
WWWWW
WWGWW
[['W', 'W', 'G', 'W', 'W'], 
['W', 'G', 'W', 'W', 'W'], 
['W', 'G', 'W', 'G', 'W'], 
['W', 'W', 'W', 'W', 'W'], 
['W', 'W', 'G', 'W', 'W']]

GGB
GGW
WWW

[['G', 'W', 'G'], 
['G', 'G', 'W'], 
['W', 'W', 'W']]
'''
        
for _ in range(int(input())):
    # print("-")
    t  = solve()
    print(t)
    #print("YES" if t else "NO")
    #print("NO" if t else "NO")