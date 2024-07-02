#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

const int MAXN = 200006;
vector<int> adj[MAXN];
int dp[MAXN];

pair<int, int> bfs(int node, int N) {
    queue<pair<int, int>> q;
    q.push({node, 0});
    unordered_set<int> vis;
    vis.insert(node);

    int max_dis = 0;
    int max_node = node;

    while (!q.empty()) {
        int i = q.front().first;
        int d = q.front().second;
        q.pop();

        if (d > max_dis) {
            max_dis = d;
            max_node = i;
        }

        for (int v : adj[i]) {
            if (vis.find(v) == vis.end()) {
                vis.insert(v);
                q.push({v, d + 1});
            }
        }
    }

    return {max_node, max_dis};
}

void bfs_update_distance(int node, int N) {
    queue<pair<int, int>> q;
    q.push({node, 0});
    unordered_set<int> vis;
    vis.insert(node);

    while (!q.empty()) {
        int i = q.front().first;
        int d = q.front().second;
        q.pop();

        dp[i] = max(dp[i], d);

        for (int v : adj[i]) {
            if (vis.find(v) == vis.end()) {
                vis.insert(v);
                q.push({v, d + 1});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    for (int i = 0; i < N - 1; ++i) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    fill(dp, dp + N + 1, 0);

    pair<int, int> a = bfs(1, N);
    pair<int, int> b = bfs(a.first, N);

    bfs_update_distance(a.first, N);
    bfs_update_distance(b.first, N);

    for (int i = 1; i <= N; ++i) {
        cout << dp[i] << " ";
    }
    cout << endl;

    return 0;
}
