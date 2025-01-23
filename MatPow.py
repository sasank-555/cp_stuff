MOD1 = 10**9 + 7
def matmul(a,b):
    n = len(a)
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = sum(a[i][k]*b[k][j] for k in range(n))%MOD1
    return ans
def matpow(base,p):
    n = len(base)
    ans = [[0]*n for _ in range(n)]
    for i in range(n) : ans[i][i] = 1
    while p :
        if p & 1:
            ans = matmul(ans,base)
        base = matmul(base,base)
        p//=2
    return ans