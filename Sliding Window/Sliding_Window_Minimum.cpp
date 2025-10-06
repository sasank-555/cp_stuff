#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    
    long long x, a, b, c;
    cin >> x >> a >> b >> c;

    deque<long long> q;
    vector<long long> nums;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long element = (i > 0 ? (a * nums.back() + b) % c : x);

        while (!q.empty() && q.back() > element) {
            q.pop_back();
        }
        q.push_back(element);

        if (i >= k && q.front() == nums[i - k]) {
            q.pop_front();
        }

        if (i >= k - 1) {
            ans ^= q.front();
        }

        nums.push_back(element);
    }

    cout << ans << endl;
    return 0;
}
