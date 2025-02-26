#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> getSubSeq(const vector<long long>& s) {
    vector<long long> st;
    for (long long x : s) {
        while (!st.empty() && x > st.back()) {
            st.pop_back();
        }
        st.push_back(x);
    }
    return st;
}

void solve() {
    int n;
    cin >> n;
    vector<long long> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    if (n == 1) {
        cout << nums[0] << "\n";
        return;
    }
    
    // Build array "aa" as pairs {number, original index}
    vector<pair<long long,int>> aa;
    for (int i = 0; i < n; i++) {
        aa.push_back({nums[i], i});
    }
    // Sort by descending number and then ascending index
    sort(aa.begin(), aa.end(), [](const pair<long long,int>& a, const pair<long long,int>& b) {
        if (a.first == b.first)
            return a.second < b.second;
        return a.first > b.first;
    });
    
    vector<long long> ans = getSubSeq(nums);
    int mx = -1;
    for (int i = 0; i < n - 1; i++) {
        if (aa[i].second > i && aa[i+1].second < aa[i].second) {
            // Remove element at index aa[i].second
            nums.erase(nums.begin() + aa[i].second);
            int j = i + 1;
            while (j < (int)aa.size()) {
                if (aa[j].second > mx)
                    break;
                j++;
            }
            if (j < aa.size() && aa[j].second > mx) {
                // Insert the value at position aa[j].second
                nums.insert(nums.begin() + aa[j].second, aa[i].first);
            }
            break;
        } else {
            mx = max(mx, aa[i].second);
        }
    }
    vector<long long> cand = getSubSeq(nums);
    if (cand > ans)
        ans = cand;
    
    for(int i = 0;i < ans.size();i++){
        cout<<ans[i];
        if (i!=ans.size() - 1) cout<<" ";
        
    }
    cout << "\n";
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