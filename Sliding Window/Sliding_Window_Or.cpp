#include <bits/stdc++.h>
using namespace std;
using lli = long long;
int main() {
    int n, k;
    cin >> n >> k;
    
    long long x, a, b, c;
    cin >> x >> a >> b >> c;
    vector<long long> nums;
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        long long element = (i > 0 ? (a * nums.back() + b) % c : x);
        nums.push_back(element);
    }
    vector<int> cnt(32,0);
    function<void(lli)> add = [&](lli x){
        for(int i = 0 ; i < 32 ; i ++){
            if(x & (1LL << i)){
                cnt[i]+=1;
            }
        }
    };
    function<void(lli)> remove = [&](lli x){
        for(int i = 0 ; i < 32 ; i ++){
            if(x & (1LL << i)){
                cnt[i]-=1;
            }
        }
    };

    function<lli()> ok = [&]()->lli{
        lli ret = 0;
        for(int i = 0 ; i < 32 ; i ++){
            if(cnt[i] > 0){
                ret+=(1LL << i);
            }
        }
        return ret;

    };

    for(int i = 0 ; i < k ;i ++){
        add(nums[i]);
    }
    ans  = ok();
    for(int i  = k ; i < nums.size() ; i++){
        remove(nums[i-k]);
        add(nums[i]);
        ans = ans ^ ok();
    }
    cout << ans << endl;
    return 0;
}
