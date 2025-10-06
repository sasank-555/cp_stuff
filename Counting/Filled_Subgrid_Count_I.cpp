#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j < n; ++j) {
            grid[i][j] = s[j] - 'A';
        }
    }
    for (int curr = 0; curr < k; ++curr) {
        long long ans = 0;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (grid[i][j] == curr) {
                    int a = (i + 1 < n) ? dp[i + 1][j] : 0;
                    int b = (j + 1 < n) ? dp[i][j + 1] : 0;
                    int c = (i + 1 < n && j + 1 < n) ? dp[i + 1][j + 1] : 0;
                    dp[i][j] = 1 + min({a, b, c});
                    ans += dp[i][j];
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}