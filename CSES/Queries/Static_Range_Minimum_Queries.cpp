#include <iostream>
#include <vector>
#include <climits> // For INT_MAX and INT_MIN
using namespace std;

class SegmentTree {
    vector<long long> tree;
    int n;
    long long (*fn)(long long, long long);

    void build(const vector<int>& nums, int index, int low, int high) {
        if (low == high) {
            tree[index] = nums[low];
        } else {
            int mid = (low + high) / 2;
            build(nums, 2 * index + 1, low, mid);
            build(nums, 2 * index + 2, mid + 1, high);
            tree[index] = fn(tree[2 * index + 1], tree[2 * index + 2]);
        }
    }

    long long rangeQuery_(int index, int low, int high, int left, int right) {
        // Complete overlap
        if (low >= left && high <= right) {
            return tree[index];
        }
        // No overlap
        if (low > right || high < left) {
            if (fn == minFn) return LLONG_MAX;
            if (fn == maxFn) return LLONG_MIN;
            return 0;
        }
        // Partial overlap
        int mid = (low + high) / 2;
        long long l = rangeQuery_(2 * index + 1, low, mid, left, right);
        long long r = rangeQuery_(2 * index + 2, mid + 1, high, left, right);
        return fn(l, r);
    }

    void update_(int i, long long val, int index, int low, int high) {
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
        tree[index] = fn(tree[2 * index + 1], tree[2 * index + 2]);
    }

public:
    SegmentTree(const vector<int>& nums, long long (*func)(long long, long long)) {
        n = nums.size();
        fn = func;
        tree.resize(4 * n);
        build(nums, 0, 0, n - 1);
    }

    long long rangeQuery(int left, int right) {
        return rangeQuery_(0, 0, n - 1, left, right);
    }

    void update(int i, long long val) {
        update_(i, val, 0, 0, n - 1);
    }

    static long long minFn(long long a, long long b) {
        return min(a, b);
    }

    static long long maxFn(long long a, long long b) {
        return max(a, b);
    }
};

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    SegmentTree st(arr, SegmentTree::minFn);

    while (q--) {
        int l, r;
        cin >> l >> r;
        l--, r--;
        cout << st.rangeQuery(l, r) << endl;
    }

    return 0;
}
