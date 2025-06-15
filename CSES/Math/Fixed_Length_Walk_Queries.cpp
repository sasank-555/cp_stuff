#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (ll)1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // dis[src][node*2 + parity] = shortest distance with given parity
    vector<vector<ll>> dis(n, vector<ll>(2 * n, INF));

    vector<int> curr, next;
    for (int src = 0; src < n; src++) {
        auto &d = dis[src];
        curr.clear();
        d[src * 2] = 0;
        curr.push_back(src * 2);

        while (!curr.empty()) {
            next.clear();
            for (int u : curr) {
                int node = u / 2;
                ll dist_u = d[u];
                for (int v : adj[node]) {
                    ll nd = dist_u + 1;
                    int idx = v * 2 + (nd % 2);
                    if (nd < d[idx]) {
                        d[idx] = nd;
                        next.push_back(idx);
                    }
                }
            }
            curr.swap(next);
        }
    }

    while (q--) {
        int a, b, x;
        cin >> a >> b >> x;
        --a; --b;
        ll even_d = dis[a][b * 2];
        ll odd_d  = dis[a][b * 2 + 1];
        bool ok = (x >= even_d && (x - even_d) % 2 == 0)
               || (x >= odd_d  && (x - odd_d)  % 2 == 0);
        cout << (ok ? "YES" : "NO") << '\n';
    }

    return 0;
}
