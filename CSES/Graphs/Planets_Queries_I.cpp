#include <bits/stdc++.h>
using namespace std;

const int LOG = 30; 
void solve() {
    int n, q;
    cin >> n >> q;

    vector<vector<int>> par(n + 1, vector<int>(LOG));
    for (int i = 1; i <= n; ++i) {
        cin >> par[i][0];
    }

    for (int j = 1; j < LOG; ++j) {
        for (int i = 1; i <= n; ++i) {
            par[i][j] = par[par[i][j - 1]][j - 1];
        }
    }

    while (q--) {
        int x, k;
        cin >> x >> k;

        for (int i = LOG - 1; i >= 0; --i) {
            if (k & (1 << i)) {
                x = par[x][i];
            }
        }

        cout << x << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}