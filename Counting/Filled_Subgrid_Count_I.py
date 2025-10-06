n,k = map(int,input().split())
grid = []
for _ in range(n):
    s = list(map(lambda x : ord(x) - ord('A'),list(input())))
    grid.append(s)
ans = [0]*k
dp =[[0]*n for _ in range(n)]
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        a = dp[i + 1][j] if i + 1 < n and grid[i + 1][j]==grid[i][j] else 0
        b = dp[i][j + 1] if j + 1 < n  and grid[i][j + 1]==grid[i][j] else 0
        c = dp[i + 1][j + 1] if i + 1 < n  and j + 1<n and grid[i + 1][j + 1]==grid[i][j]   else 0
        dp[i][j] = 1 + min(a,b,c)
        ans[grid[i][j]]+=dp[i][j]
for i in range(k):print(ans[i])