#include <bits/stdc++.h>
using namespace std;

#define MOD1 1000000007
#define INF 1e17

int erap(string &s, int d) {
    int N = s.size();
    vector<vector<vector<int>>> dp(N + 1, vector<vector<int>>(2, vector<int>(d, -1)));

    function<int(int, bool, int)> go = [&](int idx, bool tight, int rem) -> int {
        if (dp[idx][tight][rem] != -1)
            return dp[idx][tight][rem];
        if (idx == N)
            return rem == 0 ? 1 : 0;

        int md = tight ? s[idx] - '0' : 9;
        int ans = 0;

        for (int j = 0; j <= md; ++j) {
            ans = (ans + go(idx + 1, tight && (j == s[idx] - '0'), (rem + j) % d)) % MOD1;
        }

        dp[idx][tight][rem] = ans;
        return ans;
    };

    return (go(0, true, 0) - 1 + MOD1) % MOD1;
}

void solve() {
    string r;
    int d;
    cin >> r >> d;

    cout << erap(r, d) << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t = 1; 
    while (t--) {
        solve();
    }

    return 0;
}
