#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define INF 1e9

int input() {
    int x;
    cin >> x;
    return x;
}

int lefty(int i, int j, int n) {
    return (j - i + n) % n;
}

void solve() {
    int n = input();
    vector<int> a(n), b(n);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }
    
    vector<vector<int>> pt(n, vector<int>(n + 1, 0));
    vector<int> re = a;
    reverse(re.begin(), re.end());
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            pt[i][j + 1] = pt[i][j] + (re[j] == b[j]);
        }
        rotate(re.begin(), re.begin() + 1, re.end());
    }

    vector<int> ans(n + 1, 0);
    vector<int> p(n + 1, 0);

    for (int i = 0; i < n; i++) {
        p[i + 1] = p[i] + (a[i] == b[i]);
    }
    
    int tot = p[n];
    for (int l = 0; l < n; l++) {
        for (int r = l; r < n; r++) {
            int delta = lefty(l, n - r - 1, n);
            int uff = pt[delta][r + 1] - pt[delta][l] + tot - (p[r + 1] - p[l]);
            ans[uff]++;
        }
    }    
    for (int x : ans) {
        cout << x << endl;
    }
}
int main() {
    solve();
    return 0;
}
