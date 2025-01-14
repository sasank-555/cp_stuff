#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define pii pair<int, int>
#define INF 1e17
#define MOD1 1000000007
#define MOD2 998244353

void solve() {
    int n, q;
    cin >> n >> q;
    vll nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];

    int LOG = 32 - __builtin_clz(n) + 1;
    vi nge(n, n);
    vll p(n + 1, 0);
    vector<vi> parent(n + 1, vi(LOG, n));
    vector<vll> ops(n + 1, vll(LOG, 0));

    // Calculate next greater element (NGE) to the right
    stack<int> st;
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && nums[st.top()] <= nums[i]) st.pop();
        if (!st.empty()) nge[i] = st.top();
        st.push(i);
    }

    // Preprocess parent and ops tables
    for (int i = 0; i < n; ++i) {
        p[i + 1] = p[i] + nums[i];
        ops[i][0] = nums[i] * (nge[i] - i);
        parent[i][0] = nge[i];
    }

    for (int l = 1; l < LOG; ++l) {
        for (int i = 0; i < n; ++i) {
            ops[i][l] = ops[i][l - 1] + ops[parent[i][l - 1]][l - 1];
            parent[i][l] = parent[parent[i][l - 1]][l - 1];
        }
    }

    // Answer queries
    while (q--) {
        int l, r;
        cin >> l >> r;
        --l, --r;
        int curr = l;
        ll cost = 0;

        for (int lll = LOG - 1; lll >= 0; --lll) {
            if (parent[curr][lll] <= r) {
                cost += ops[curr][lll];
                curr = parent[curr][lll];
            }
        }

        cost += (r - curr + 1) * nums[curr];
        cost -= (p[r + 1] - p[l]);

        cout << cost << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}
