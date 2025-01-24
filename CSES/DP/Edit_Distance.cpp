#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int solve(const string& s, const string& t) {
    int m = s.size();
    int n = t.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));

    for (int i = m; i >= 0; --i) {
        for (int j = n; j >= 0; --j) {
            if (j == n) {
                dp[i][j] = m - i;
            } else if (i == m) {
                dp[i][j] = n - j;
            } else {
                if (s[i] == t[j]) {
                    dp[i][j] = dp[i + 1][j + 1];
                } else {
                    dp[i][j] = 1 + min({dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1]});
                }
            }
        }
    }

    return dp[0][0];
}

int main() {
    string s, t;
    cin >> s >> t;
    int result = solve(s, t);
    cout << result << endl;
    return 0;
}