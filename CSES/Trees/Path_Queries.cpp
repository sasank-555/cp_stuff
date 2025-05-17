#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class SegmentTree {
private:
    vector<ll> tree;
    int n;
    
    void build(vector<ll>& nums, int index, int low, int high) {
        if (low == high) {
            tree[index] = nums[low];
            return;
        }
        int mid = (low + high) / 2;
        build(nums, 2 * index + 1, low, mid);
        build(nums, 2 * index + 2, mid + 1, high);
        tree[index] = tree[2 * index + 1] + tree[2 * index + 2];
    }
    
    ll rangeQuery_(int index, int low, int high, int left, int right) {
        if (low >= left && high <= right) {
            return tree[index];
        }
        if (low > right || high < left) {
            return 0;
        }
        int mid = (low + high) / 2;
        ll l = rangeQuery_(2 * index + 1, low, mid, left, right);
        ll r = rangeQuery_(2 * index + 2, mid + 1, high, left, right);
        return l + r;
    }
    
    void update_(int i, ll val, int index, int low, int high) {
        if (low == high) {
            tree[index] = val;
            return;
        }
        int mid = (low + high) / 2;
        if (i > mid) {
            update_(i, val, 2 * index + 2, mid + 1, high);
        } else {
            update_(i, val, 2 * index + 1, low, mid);
        }
        tree[index] = tree[2 * index + 1] + tree[2 * index + 2];
    }
    
public:
    SegmentTree(vector<ll>& nums) {
        n = nums.size();
        tree.resize(4 * n);
        build(nums, 0, 0, n - 1);
    }
    
    ll rangeQuery(int left, int right) {
        return rangeQuery_(0, 0, n - 1, left, right);
    }
    
    void update(int i, ll val) {
        update_(i, val, 0, 0, n - 1);
    }
};

void solve() {
    int n, q;
    cin >> n >> q;
    
    vector<ll> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        x--; y--;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    
    vector<int> parent(n, -1);
    vector<int> intime(n), outtime(n);
    vector<ll> vals(2 * n);
    
    int timer = -1;
    stack<int> st;
    st.push(0);
    
    while (!st.empty()) {
        int u = st.top();
        st.pop();
        
        if (u >= 0) {
            timer++;
            intime[u] = timer;
            vals[timer] = nums[u];
            st.push(~u);
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    st.push(v);
                    parent[v] = u;
                }
            }
        } else {
            u = ~u;
            timer++;
            vals[timer] = -nums[u];
            outtime[u] = timer;
        }
    }
    
    SegmentTree segTree(vals);
    
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int s, x;
            cin >> s >> x;
            s--;
            segTree.update(intime[s], x);
            segTree.update(outtime[s], -x);
        } else {
            int s;
            cin >> s;
            s--;
            cout << segTree.rangeQuery(0, intime[s]) << "\n";
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t = 1;
    while (t--) {
        solve();
    }
    return 0;
}