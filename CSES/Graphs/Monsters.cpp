#include <bits/stdc++.h>
using namespace std;

#define INF 1e17
#define MOD1 1000000007
#define MOD2 998244353
#define fastio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

typedef long long ll;
typedef pair<int, int> pii;

vector<vector<int>> dirs;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<string> grid(n);

    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    deque<tuple<int, int, int>> q;
    vector<vector<ll>> dis(n, vector<ll>(m, INF));

    dirs.push_back(vector<int>{0, 1});
    dirs.push_back(vector<int>{1, 0});
    dirs.push_back(vector<int>{-1, 0});
    dirs.push_back(vector<int>{0, -1});

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'M') {
                q.push_back(make_tuple(i, j, 0));
                dis[i][j] = 0;
            }
        }
    }

    while (!q.empty()) {
        tuple<int, int, int> curr = q.front();
        q.pop_front();
        int x = get<0>(curr);
        int y = get<1>(curr);
        int d = get<2>(curr);

        for (size_t k = 0; k < dirs.size(); k++) {
            int nx = x + dirs[k][0];
            int ny = y + dirs[k][1];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && 1 + d < dis[nx][ny] && grid[nx][ny] != '#') {
                dis[nx][ny] = 1 + d;
                q.push_back(make_tuple(nx, ny, 1 + d));
            }
        }
    }

    deque<tuple<int, int, int, int, int>> q2;
    set<pii> vis;
    map<pii, pii> par;
    int curri = -1, currj = -1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'A') {
                q2.push_back(make_tuple(0, i, j, -1, -1));
                vis.insert(make_pair(i, j));
                break;
            }
        }
    }

    while (!q2.empty()) {
        tuple<int, int, int, int, int> curr = q2.front();
        q2.pop_front();
        int d = get<0>(curr);
        int i = get<1>(curr);
        int j = get<2>(curr);
        int pi = get<3>(curr);
        int pj = get<4>(curr);
        par[make_pair(i, j)] = make_pair(pi, pj);

        if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
            curri = i;
            currj = j;
            break;
        }

        for (size_t k = 0; k < dirs.size(); k++) {
            int nx = i + dirs[k][0];
            int ny = j + dirs[k][1];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && vis.count(make_pair(nx, ny)) == 0 && 1 + d < dis[nx][ny] && grid[nx][ny] != '#') {
                q2.push_back(make_tuple(1 + d, nx, ny, i, j));
                vis.insert(make_pair(nx, ny));
            }
        }
    }

    if (curri == -1) {
        cout << "NO" << endl;
        return;
    }

    cout << "YES" << endl;

    vector<char> ans;
    while (true) {
        pii parent = par[make_pair(curri, currj)];
        int pi = parent.first;
        int pj = parent.second;
        if (pi == -1) break;

        if (curri == pi + 1) ans.push_back('D');
        else if (currj == pj + 1) ans.push_back('R');
        else if (curri == pi - 1) ans.push_back('U');
        else if (currj == pj - 1) ans.push_back('L');

        curri = pi;
        currj = pj;
    }

    reverse(ans.begin(), ans.end());
    cout << ans.size() << endl;
    for (size_t i = 0; i < ans.size(); i++) {
        cout << ans[i];
    }
    cout << endl;
}

int main() {
    fastio;
    int t = 1;
    while (t--) {
        solve();
    }
    return 0;
}
