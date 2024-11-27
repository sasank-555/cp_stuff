#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

const int WHITE = 0, BLACK = 1, GREY = 2;
const long long INF = 1e17;

bool dfs(int curr, int p, vector<int>& color, vector<int>& path, vector<vector<int>>& adj) {
    color[curr] = GREY;
    path.push_back(curr);

    for (int v : adj[curr]) {
        if (color[v] == WHITE) {
            if (dfs(v, curr, color, path, adj)) {
                return true;
            }
        } else if (color[v] == GREY && v != p) {
            // A cycle has been detected
            vector<int> cycle;
            int cycle_start = v;
            cycle.push_back(cycle_start);
            for (int i = path.size() - 1; i >= 0; --i) {
                cycle.push_back(path[i]);
                if (path[i] == cycle_start) {
                    break;
                }
            }
            reverse(cycle.begin(), cycle.end());
            cout << cycle.size() << "\n";
            for (int node : cycle) {
                cout << node << " ";
            }
            cout << endl;
            return true;
        }
    }

    color[curr] = BLACK;
    path.pop_back();
    return false;
}

void solve() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    vector<int> color(n + 1, WHITE);
    bool cycle_dete = false;

    for (int i = 1; i <= n; ++i) {
        if (color[i] == WHITE) {
            vector<int> path;
            if (dfs(i, -1, color, path, adj)) {
                cycle_dete = true;
                break;
            }
        }
    }

    if (!cycle_dete) {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}
