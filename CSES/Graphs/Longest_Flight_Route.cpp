#include <bits/stdc++.h>
using namespace std;

const int MOD1 = 1e9 + 7;
const int MOD2 = 998244353;
const long long INF = 1e17;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
    }
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> q;
    q.push({0, 1});
    vector<long long> dp(n + 1, 0);
    vector<int> came(n + 1, -1);
    dp[1] = 0;
    while (!q.empty()) {
        pair<int, int> top = q.top();
        q.pop();
        int c = top.first;
        int u = top.second;
        if(c > dp[u]) continue;
        for (int v : adj[u]) {
            if (dp[v] > c - 1) {
                dp[v] = c - 1;
                came[v] = u;
                q.push({c - 1, v});
            }
        }
    }
    if (dp[n] == 0) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    vector<int> ans;
    int curr = n;
    while (curr != -1) {
        ans.push_back(curr);
        curr = came[curr];
    }
    cout << -dp[n] + 1 << endl;
    reverse(ans.begin(), ans.end());
    for (int x : ans) {
        cout << x << " ";
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}