#include <bits/stdc++.h>
using namespace std;
using lli = long long;
int main() {
    lli k , n;
    cin>>n>>k;
    vector<lli> nums(n);
    for(auto & x : nums)cin>>x;
    set<lli> missing;
    map<int,int> f;
    for(int i = 0 ; i < n ; i ++){
        missing.insert(i);
        if (i < k) f[nums[i]]+=1;
    }
    for(auto x : f){
        int val = x.first;
        missing.erase(val);
    }
    vector<int> ans;
    ans.push_back(*missing.begin());
    for(int i  = k ; i < n ; i ++){
        f[nums[i-k]]-=1;
        if(f[nums[i-k]]==0){
            missing.insert(nums[i-k]);
        }
        if(f[nums[i]]==0){
            missing.erase(nums[i]);
        }
        f[nums[i]]+=1;
        ans.push_back(*missing.begin());
    }
    for(auto x : ans){
        cout<<x<<" ";
    }
    cout<<endl;
}
