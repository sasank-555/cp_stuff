#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

const int MOD1 = 1e9 + 7;
const int MOD2 = 998244353;
const long long INF = 1e17;
const int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

// BFS function to find the shortest path to 'B'
pair<int, int> bfs(int si, int sj, int n, int m, const vector<vector<char>>& grid, vector<vector<bool>>& vis, map<pair<int, int>, pair<int, int>>& parent) {
    queue<pair<int, int>> q;
    q.push(make_pair(si, sj));
    vis[si][sj] = true;

    while (!q.empty()) {
        pair<int, int> current = q.front();
        q.pop();

        int i = current.first;
        int j = current.second;

        if (grid[i][j] == 'B') {
            return make_pair(i, j);
        }

        for (int k = 0; k < 4; ++k) {
            int ni = i + dirs[k][0];
            int nj = j + dirs[k][1];

            if (ni >= 0 && ni < n && nj >= 0 && nj < m && !vis[ni][nj] && grid[ni][nj] != '#') {
                vis[ni][nj] = true;
                q.push(make_pair(ni, nj));
                parent[make_pair(ni, nj)] = make_pair(i, j);
            }
        }
    }
    return make_pair(-1, -1); // No path to 'B' found
}

void solve() {
    int n, m;
    cin >> n >> m;

    vector<vector<char>> grid(n, vector<char>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
        }
    }

    vector<vector<bool>> vis(n, vector<bool>(m, false));
    map<pair<int, int>, pair<int, int>> parent;
    map<pair<int, int>, string> d;
    d[make_pair(0, 1)] = "R";
    d[make_pair(0, -1)] = "L";
    d[make_pair(1, 0)] = "D";
    d[make_pair(-1, 0)] = "U";

    int si = -1, sj = -1, bi = -1, bj = -1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'A') {
                si = i;
                sj = j;
            } else if (grid[i][j] == 'B') {
                bi = i;
                bj = j;
            }
        }
    }

    pair<int, int> endpoint = bfs(si, sj, n, m, grid, vis, parent);
    int ei = endpoint.first, ej = endpoint.second;

    if (ei == -1 && ej == -1) {
        cout << "NO" << endl;
        return;
    }

    // Reconstruct the path from 'B' to 'A'
    vector<string> path;
    pair<int, int> cur = make_pair(ei, ej);
    while (cur != make_pair(si, sj)) {
        pair<int, int> prev = parent[cur];
        int di = cur.first - prev.first;
        int dj = cur.second - prev.second;
        path.push_back(d[make_pair(di, dj)]);
        cur = prev;
    }

    reverse(path.begin(), path.end());
    cout << "YES" << endl;
    cout << path.size() << endl;
    for (int i = 0; i < path.size(); ++i) {
        cout << path[i];
    }
    cout << endl;
}

int main() {
    solve();
    return 0;
}
