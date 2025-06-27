mod = 10**9 + 7
fact  = [0]*(1001)
fact[0] = fact[1] = 1
for i in range(2,1001):
    fact[i] = i*fact[i-1]
    fact[i]%=mod
dp = [[0]*1001 for _ in range(1001)]
# dp[s][t]: Number of ways to divide `s` people into `t` teams(teams are identical people are distinct)
inv = [0]*1001
for i in range(1001):
    inv[i] = pow(fact[i],-1,mod)
dp[0][0] = 1
for s in range(1,1001):
    for t in range(1,1001):
        dp[s][t] = dp[s-1][t-1] + t*(dp[s-1][t])
        dp[s][t]%=mod