#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9 + 7;  // Large number to represent infinity

void solve() {
    int n, m, q;
    cin >> n >> m >> q;

    // Distance matrix initialization with INF
    vector<vector<int>> dis(n + 1, vector<int>(n + 1, INF));

    // Read the edges and populate the distance matrix
    for (int i = 0; i < m; i++) {
        int x, y, w;
        cin >> x >> y >> w;

        // Ensure that if there's already an edge between x and y, we take the minimum weight
        dis[x][y] = min(dis[x][y], w);
        dis[y][x] = min(dis[y][x], w);
    }

    // Distance from a node to itself is 0
    for (int i = 1; i <= n; i++) {
        dis[i][i] = 0;
    }

    // Floyd-Warshall algorithm to find all-pairs shortest paaths
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                // Update the distance matrix with the shortest path
                if (dis[i][k] != INF && dis[k][j] != INF) {
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
            }
        }
    }

    // Processing the queries
    while (q--) {
        int fr, to;
        cin >> fr >> to;

        // Output -1 if no path exists (INF indicates no path)
        if (dis[fr][to] == INF) {
            cout << -1 << endl;
        } else {
            cout << dis[fr][to] << endl;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);  // Fast I/O
    cin.tie(0);  // Disable unnecessary cin flushing

    solve();
    
    return 0;
}
