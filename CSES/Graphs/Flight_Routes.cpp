#include <bits/stdc++.h>
using namespace std;

#define INF LLONG_MAX
#define MOD1 1000000007
#define MOD2 998244353

typedef long long ll;
typedef pair<ll, ll> pll;

void solve() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<pll>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        ll a, b, c;
        cin >> a >> b >> c;
        adj[a].emplace_back(b, c);
    }

    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> pq; // {cost, node}
    pq.push(make_pair(0, 1));

    vector<vector<ll>> dp(n + 1, vector<ll>(k, INF));
    dp[1][0] = 0;

    while (!pq.empty()) {
        pair<ll, ll> top = pq.top();
        pq.pop();
        ll c = top.first;
        ll u = top.second;

        if (c > dp[u][k - 1]) continue;

        for (size_t i = 0; i < adj[u].size(); ++i) {
            ll v = adj[u][i].first;
            ll w = adj[u][i].second;
            if (dp[v][k - 1] > c + w) {
                dp[v][k - 1] = c + w;
                sort(dp[v].begin(), dp[v].end());
                pq.push(make_pair(c + w, v));
            }
        }
    }

    for (int i = 0; i < k; ++i) {
        cout << dp[n][i] << " ";
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    while (t--) {
        solve();
    }

    return 0;
}
