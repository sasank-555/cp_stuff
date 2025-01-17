#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200001; 
const int LOG = 20;     

vector<int> adj[MAXN];   
int par[MAXN][LOG];      
int lvl[MAXN];          

void dfs(int node, int parent) {
    par[node][0] = parent;
    for (int neighbor : adj[node]) {
        if (neighbor != parent) {
            lvl[neighbor] = lvl[node] + 1;
            dfs(neighbor, node);
        }
    }
}

void compute_parents(int n) {
    for (int l = 1; l < LOG; l++) {
        for (int i = 1; i <= n; i++) {
            if (par[i][l - 1] != -1) {
                par[i][l] = par[par[i][l - 1]][l - 1];
            }
        }
    }
}

int lca(int u, int v) {
    if (lvl[u] < lvl[v]) {
        swap(u, v);
    }

    for (int i = LOG - 1; i >= 0; i--) {
        if ((lvl[u] - lvl[v]) & (1 << i)) {
            u = par[u][i];
        }
    }

    if (u == v) {
        return u;
    }

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
    int x ,y;
    for (int i = 0; i < n - 1; i++) {
        cin>>x>>y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    memset(par, -1, sizeof(par));
    lvl[1] = 0;
    dfs(1, -1);
    compute_parents(n);

    while (q--) {
        int u, v;
        cin >> u >> v;
        cout<< lvl[u] + lvl[v] -2*lvl[lca(u, v)]<<"\n";
    }

    return 0;
}
