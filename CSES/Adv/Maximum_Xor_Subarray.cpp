#include <bits/stdc++.h>
using namespace std;

struct Node {
    Node* children[2];
    Node() {
        children[0] = children[1] = nullptr;
    }
};

void insert(Node* root, int val) {
    Node* curr = root;
    for(int i = 31; i >= 0; i--) {
        int bit = (val >> i) & 1;
        if(!curr->children[bit]) {
            curr->children[bit] = new Node();
        }
        curr = curr->children[bit];
    }
}

int getMaxXor(Node* root, int val) {
    Node* curr = root;
    int ans = 0;
    for(int i = 31; i >= 0; i--) {
        int bit = (val >> i) & 1;
        int opposite = bit ^ 1;
        
        if(curr->children[opposite]) {
            ans |= (1 << i);
            curr = curr->children[opposite];
        }
        else if(curr->children[bit]) {
            curr = curr->children[bit];
        }
        else break;
    }
    return ans;
}

void solve() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    vector<int> p(n + 1, 0);
    for(int i = 0; i < n; i++) {
        p[i + 1] = p[i] ^ nums[i];
    }
    
    Node* root = new Node();
    int mx = 0;
    
    for(int i = 0; i < p.size(); i++) {
        mx = max(mx, getMaxXor(root, p[i]));
        insert(root, p[i]);
    }
    
    cout << mx << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t = 1;
    while(t--) {
        solve();
    }
    return 0;
}