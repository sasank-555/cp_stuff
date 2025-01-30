#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

void solve() {
    long long n, m;
    cin >> n >> m;
    vector<long long> a(n);
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    long long best = LLONG_MAX;
    vector<long long> r(n);
    for(int i = 0; i < n; i++) {
        r[i] = a[i] % m;
    }
    sort(r.begin(), r.end());
    
    vector<long long> p(n + 1, 0);
    for(int i = 0; i < n; i++) {
        p[i + 1] = p[i] + r[i];
    }
    
    for(int i = 0; i < n; i++) {
        long long curr = 0;
        int l = i;
        int rr = n - 1;
        int temp = l;
        
        while(l <= rr) {
            int mid = (l + rr) / 2;
            if(r[mid] - r[i] <= m + r[i] - r[mid]) {
                temp = mid;
                l = mid + 1;
            } else {
                rr = mid - 1;
            }
        }
        
        curr += p[temp + 1] - p[i] - (long long)(temp - i + 1) * r[i];
        curr += (long long)(r[i] + m) * (n - (temp + 1)) - (p[n] - p[temp + 1]);
        
        l = 0;
        rr = i;
        int temp2 = i;
        
        while(l <= rr) {
            int mid = (l + rr) / 2;
            if(r[i] - r[mid] <= m - (r[i] - r[mid])) {
                rr = mid - 1;
                temp2 = mid;
            } else {
                l = mid + 1;
            }
        }
        
        curr += (long long)(i + 1 - temp2) * r[i] - (p[i + 1] - p[temp2]);
        curr += (long long)(m - r[i]) * temp2 + p[temp2];
        best = min(best, curr);
    }
    cout << best << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while(t--) {
        solve();
    }
    return 0;
}