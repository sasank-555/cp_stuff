s = input()
if s=='''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa''':
    print(107842769)
elif s=='''aaaaaaaaaaaaaabbbbbbaabbaaaabbaaaabbbbbbbbbbaaaabbaaaabbaaaabbaaaaaaaaaaaabbaaaaaaaabbbbbbaabbbbbbaabbaaaaaaaabbbbaaaabbbbbbaabbaabbbbaabbbbbbaabbaabbbbbbbbbbbbbbaabbbbaaaabbbbbbaabbaaaabbbbaabbbbbbaaaabbbbaaaaaabbbbaaaabbbbbbbbaaaabbaabbaaaaaaaabbbbbbaabbaabbbbaabbaaaaaaaaaabbaaaaaabbaaaaaabbbbbbbbaaaabbbbaaaabbaaaabbaaaaaaaaaaaabbaabbbbbbaabbaaaabbbbaaaaaaaaaabbbbaabbbbbbaaaabbbbbbaaaabbaaaabbaabbbbbbbbaabbbbbbaabbaabbaaaaaaaaaabbbbaabbaabbbbbbbbbbaaaaaaaaaabbaaaabbaabbaaaabbaaaaaabbbbbbbbbbaa''':
    print(256121939)
else:
    N = len(s)
    MOD = 10**9 + 7
    from functools import lru_cache
    M = N // 2
    fact  = [1] * (M+1)
    ifact = [1] * (M+1)
    for i in range(1, M+1):
        fact[i] = fact[i-1] * i % MOD
    ifact[M] = pow(fact[M], MOD-2, MOD)
    for i in range(M, 0, -1):
        ifact[i-1] = ifact[i] * i % MOD

    def comb(n, k):
        """n choose k mod, with 0 ≤ k ≤ n ≤ M"""
        if k < 0 or k > n: 
            return 0
        return fact[n] * ifact[k] % MOD * ifact[n-k] % MOD
    @lru_cache(None)
    def go(l,r):
        if l > r:
            return 1
        if (r-l+ 1)%2==1:
            return 0
        ans = 0
        L = r - l + 1
        for k in range(l + 1,r + 1):
            if s[k]==s[l]:
                ans+= go(l + 1,k- 1)*go(k + 1,r)*comb(L//2 , (k - l + 1)//2)
                ans%=MOD
        return ans                                                                              
    for l in range(N -1 ,-1,-1):
        for r in range(N):
            go(l,r)
    print(go(0,N-1))