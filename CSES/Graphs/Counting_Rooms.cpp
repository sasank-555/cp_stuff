#include <iostream>
#include <vector>
#include <string>

using namespace std;

int dirs[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

void dfs(int i, int j, vector<vector<char>>& grid, vector<vector<bool>>& vis, int n, int m) {
    vis[i][j] = true;

    for (int d = 0; d < 4; ++d) {
        int ni = i + dirs[d][0]; 
        int nj = j + dirs[d][1]; 

        if (ni >= 0 && ni < n && nj >= 0 && nj < m && !vis[ni][nj] && grid[ni][nj] == '.') {
            dfs(ni, nj, grid, vis, n, m);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<char>> grid(n, vector<char>(m)); 
    vector<vector<bool>> vis(n, vector<bool>(m, false)); 

    // Input grid
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
        }
    }

    int cnt = 0; 

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!vis[i][j] && grid[i][j] == '.') {
                dfs(i, j, grid, vis, n, m); 
                ++cnt; 
            }
        }
    }

    cout << cnt << endl;

    return 0;
}
