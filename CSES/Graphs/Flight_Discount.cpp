#include <bits/stdc++.h>
using namespace std;

#define INF LLONG_MAX
#define MOD1 1000000007
#define MOD2 998244353

typedef long long ll;
typedef pair<ll, ll> pll;

template <typename T>
using min_heap = priority_queue<T, vector<T>, greater<T>>;

void solve() {
    int n, m;
    cin >> n >> m;

    vector<vector<pll>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        ll a, b, c;
        cin >> a >> b >> c;
        adj[a].emplace_back(b, c);
    }

    min_heap<pair<ll, pair<ll, int>>> pq; // {cost, {node, used_discount}}
    pq.emplace(make_pair(0, make_pair(1, 0)));

    vector<vector<ll>> dp(n + 1, vector<ll>(2, INF));
    dp[1][0] = 0;

    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();
        ll cost = top.first;
        ll node = top.second.first;
        int used = top.second.second;

        if (node == n) {
            cout << cost << "\n";
            return;
        }

        if (cost > dp[node][used]) continue;

        for (const auto &edge : adj[node]) {
            pair<ll, ll> edge_pair = edge;
            ll v = edge_pair.first;
            ll w = edge_pair.second;
            if (dp[v][used] > w + cost) {
                dp[v][used] = w + cost;
                pq.emplace(make_pair(dp[v][used], make_pair(v, used)));
            }

            if (used == 0 && dp[v][1] > w / 2 + cost) {
                dp[v][1] = w / 2 + cost;
                pq.emplace(make_pair(dp[v][1], make_pair(v, 1)));
            }
        }
    }

    cout << min(dp[n][0], dp[n][1]) << "\n";
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
