#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001; // Maximum number of nodes
const int LOG = 20;      // Maximum depth of the tree in binary lifting

vector<int> adj[MAXN];   // Adjacency list to store the tree
int par[MAXN][LOG];      // Binary lifting table
int lvl[MAXN];           // Level of each node

// Depth-First Search to calculate levels and initialize parent for binary lifting
void dfs(int node, int parent) {
    par[node][0] = parent;
    for (int neighbor : adj[node]) {
        if (neighbor != parent) {
            lvl[neighbor] = lvl[node] + 1;
            dfs(neighbor, node);
        }
    }
}

// Function to compute binary lifting table
void compute_parents(int n) {
    for (int l = 1; l < LOG; l++) {
        for (int i = 1; i <= n; i++) {
            if (par[i][l - 1] != -1) {
                par[i][l] = par[par[i][l - 1]][l - 1];
            }
        }
    }
}

// Function to find the Lowest Common Ancestor (LCA) of two nodes
int lca(int u, int v) {
    if (lvl[u] < lvl[v]) {
        swap(u, v);
    }

    // Lift `u` to the same level as `v`
    for (int i = LOG - 1; i >= 0; i--) {
        if ((lvl[u] - lvl[v]) & (1 << i)) {
            u = par[u][i];
        }
    }

    if (u == v) {
        return u;
    }

    // Lift both `u` and `v` together until their parents are the same
    for (int i = LOG - 1; i >= 0; i--) {
        if (par[u][i] != par[v][i]) {
            u = par[u][i];
            v = par[v][i];
        }
    }

    return par[u][0];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<int> nums(n - 1); // Input for the parent array
    for (int i = 0; i < n - 1; i++) {
        cin >> nums[i];
        adj[nums[i]].push_back(i + 2);
        adj[i + 2].push_back(nums[i]);
    }

    // Initialize parent table and level
    memset(par, -1, sizeof(par));
    lvl[1] = 0;
    dfs(1, -1);
    compute_parents(n);

    // Process queries
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << '\n';
    }

    return 0;
}
