#include <bits/stdc++.h>
using namespace std;

const int MOD1 = 1e9 + 7;

vector<vector<long long>> matmul(const vector<vector<long long>>& a, const vector<vector<long long>>& b) {
    int n = a.size();
    vector<vector<long long>> ans(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                ans[i][j] = (ans[i][j] + a[i][k] * b[k][j]) % MOD1;
            }
        }
    }
    return ans;
}

vector<vector<long long>> matpow(vector<vector<long long>> base, long long p) {
    int n = base.size();
    vector<vector<long long>> ans(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) ans[i][i] = 1;
    while (p) {
        if (p & 1) ans = matmul(ans, base);
        base = matmul(base, base);
        p >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;
    vector<vector<long long>> base(N, vector<long long>(N, 0));
    for (int i = 0; i < M; ++i) {
        int x, y;
        cin >> x >> y;
        --x; --y; // 0-based indexing
        base[x][y] += 1;
    }
    cout << matpow(base, K)[0][N-1] << '\n';
    return 0;
}