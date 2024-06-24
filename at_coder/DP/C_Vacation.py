import sys
input = sys.stdin.read

inf = float('inf')

def max_happiness(N, res):
    dp = [[-inf] * 3 for _ in range(N)]
    
    for j in range(3):
        dp[0][j] = res[0][j]
    
    
    for i in range(1, N):
        for j in range(3):
            dp[i][j] = max(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + res[i][j]
    
    return max(dp[N-1])

data = input().split()
N = int(data[0])
res = []
index = 1
for i in range(N):
    res.append([int(data[index]), int(data[index + 1]), int(data[index + 2])])
    index += 3

print(max_happiness(N, res))
