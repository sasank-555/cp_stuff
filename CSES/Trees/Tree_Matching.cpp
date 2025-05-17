#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<vector<int>> dp;
vector<vector<int>> adj;

int go(int node, int p, int t) {
    if (dp[node][t] != -1) {
        return dp[node][t];
    }

    int ans = 0;
    if (t == 1) {
        for (int v : adj[node]) {
            if (v != p) {
                go(v, node, 0);
                ans += dp[v][0];
            }
        }
    } else {
        for (int v : adj[node]) {
            if (v != p) {
                go(v, node, 0);
                ans += dp[v][0];
            }
        }
        
        int ans2 = 0;
        for (int v : adj[node]) {
            if (v != p) {
                go(v, node, 1);
                ans2 = max(ans2, 1 + dp[v][1] + ans - dp[v][0]);
            }
        }
        ans = max(ans, ans2);
    }
    
    return dp[node][t] = ans;
}

void solve() {
    int n;
    cin >> n;
    
    adj.resize(n);
    dp.assign(n, vector<int>(2, -1));
    
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        x--; y--;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    
    cout << max(go(0, -1, 0), go(0, -1, 1)) << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t = 1;
    while (t--) {
        solve();
    }
    return 0;
}