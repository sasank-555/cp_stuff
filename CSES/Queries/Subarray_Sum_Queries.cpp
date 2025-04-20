#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Node {
    ll sum, maxSum, prefixSum, suffixSum;
    Node() {
        sum = maxSum = prefixSum = suffixSum = 0;
    }
};

// Combine two nodes into one
void combine(Node& left, Node& right, Node& result) {
    result.sum = left.sum + right.sum;
    result.prefixSum = max(left.sum + right.prefixSum, left.prefixSum);
    result.suffixSum = max(right.suffixSum, right.sum + left.suffixSum);
    result.maxSum = max({left.maxSum, right.maxSum, left.suffixSum + right.prefixSum});
}

class SegmentTree {
private:
    vector<Node> tree;
    vector<ll> nums;
    int n;

    void build(int v, int tl, int tr) {
        if (tl == tr) {
            tree[v].sum = nums[tl];
            tree[v].prefixSum = nums[tl];
            tree[v].suffixSum = nums[tl];
            tree[v].maxSum = nums[tl];
            return;
        }
        
        int tm = (tl + tr) / 2;
        build(2 * v + 1, tl, tm);
        build(2 * v + 2, tm + 1, tr);
        combine(tree[2 * v + 1], tree[2 * v + 2], tree[v]);
    }

    void update(int v, int tl, int tr, int pos, ll val) {
        if (tl == tr) {
            tree[v].sum = val;
            tree[v].prefixSum = val;
            tree[v].suffixSum = val;
            tree[v].maxSum = val;
            return;
        }
        
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(2 * v + 1, tl, tm, pos, val);
        else
            update(2 * v + 2, tm + 1, tr, pos, val);
            
        combine(tree[2 * v + 1], tree[2 * v + 2], tree[v]);
    }

public:
    SegmentTree(vector<ll>& arr) {
        nums = arr;
        n = arr.size();
        tree.resize(4 * n);
        build(0, 0, n - 1);
    }

    void update(int pos, ll val) {
        update(0, 0, n - 1, pos, val);
    }

    ll getMaxSum() {
        return max(0LL, tree[0].maxSum);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    
    vector<ll> nums(n);
    for(int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    SegmentTree st(nums);
    
    while(q--) {
        int k;
        ll x;
        cin >> k >> x;
        k--;
        st.update(k, x);
        cout << st.getMaxSum() << "\n";
    }
    
    return 0;
}