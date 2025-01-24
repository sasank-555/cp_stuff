#include <bits/stdc++.h>
using namespace std;

#define MOD1 1000000007
#define MOD2 998244353
#define INF 1e17
#define all(v) v.begin(), v.end()
#define pb push_back
#define pii pair<int, int>

typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    vector<vector<int>> dp(n, vector<int>(m, 0));
    vector<vector<int>> ans(m, vector<int>(n + 1, 0));

    for (int j = 0; j < m; j++) {
        dp[n - 1][j] = (grid[n - 1][j] == '.') ? 1 : 0;
    }

    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '*') {
                dp[i][j] = 0;
            } else {
                dp[i][j] = 1 + dp[i + 1][j];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int length = 1; length <= m; length++) {
            deque<int> dq;
            for (int r = 0; r < m; r++) {
                if (!dq.empty() && dq.front() < r - length + 1) {
                    dq.pop_front();
                }
                while (!dq.empty() && dp[i][dq.back()] >= dp[i][r]) {
                    dq.pop_back();
                }
                dq.push_back(r);
                if (r >= length - 1) {
                    int mi = dp[i][dq.front()];
                    ans[length - 1][0]++;
                    ans[length - 1][mi]--;
                }
            }
        }
    }

    for (int i = 0; i < m; i++) {
        ans[i].pop_back();
        for (int j = 1; j < n; j++) {
            ans[i][j] += ans[i][j - 1];
        }
    }

    for (int j = 0; j < n; j++) {
        for (int i = 0; i < m; i++) {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t = 1;
    // cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}