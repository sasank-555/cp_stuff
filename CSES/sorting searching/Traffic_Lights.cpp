// ███████╗ █████╗ ███████╗ █████╗ ███╗   ██╗██╗  ██╗
// ██╔════╝██╔══██╗██╔════╝██╔══██╗████╗  ██║██║ ██╔╝
// ███████╗███████║███████╗███████║██╔██╗ ██║█████╔╝ 
// ╚════██║██╔══██║╚════██║██╔══██║██║╚██╗██║██╔═██╗ 
// ███████║██║  ██║███████║██║  ██║██║ ╚████║██║  ██╗
// ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
#include <bits/stdc++.h>
using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type>
ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;

// #define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
using ll = long long;
const ll MOD1 = 1e9 + 7;
const ll MOD2 = 998244353;


// Usage examples:
// int x = I();
// vector<int> nums = LII(x);
// pair<int,int> p = MII();
// vector<int> r = range(5); // {0,1,2,3,4}
// mod_add(3, 5);
// sort_by(nums, [](int x){return -x;}); // sort descending
// auto groups = group_by(nums, [](int x){return x % 2;}); // group by parity



int X,N;
void solve() {
    cin>>X>>N;
    multiset<int> ms;
    set<int> ss;
    ms.insert(X);
    ss.insert(X);
    ss.insert(0);
    for(int i = 0 ; i < N; i++){
        // dbg(ms);
        // dbg(ss);
        int k;
        cin>>k;
        auto it = ss.upper_bound(k);
        int  r = *it;
        int  l = *(--it);
        ms.erase(ms.find(r-l));
        ss.insert(k);
        ms.insert(r-k);
        ms.insert(k-l);
        cout<<*ms.rbegin()<<" ";
        // dbg(ms);
        // dbg(ss);
    }
    cout<<endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve();
        // else cout<<"NO"<<endl;
    }
}
