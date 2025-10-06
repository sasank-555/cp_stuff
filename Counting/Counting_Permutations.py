# https://oeis.org/A002464
n = int(input())
dp = [0]*(n + 1)
dp[0] = dp[1] = 1
def a(n):
    if n<=1:
        return 1
    if n in (2,3):
        return 0
    return (n+1)*a(n-1) - (n-2)*a(n-2) - (n-5)*a(n-3) + (n-3)*a(n-4)
MOD = 10**9 + 7
for i in range(4,n + 1):
    dp[i] = (i + 1)*dp[i-1] - (i-2)*dp[i-2] - (i-5)*dp[i-3]  + (i-3)*dp[i-4]
    dp[i]%=MOD
print(dp[n])
    # 1 0 0 2 14 90