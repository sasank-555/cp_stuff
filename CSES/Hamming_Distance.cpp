#include <iostream>
#include <vector>
#include <bitset>
#include <climits>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<bitset<32>> nums(n); // assuming k <= 64
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        nums[i] = bitset<32>(s);  // store binary string as bitset
    }

    int best = k;  
    
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            bitset<32> diff = nums[i] ^ nums[j];  
            best = min(best, (int)diff.count());  
        }
    }

    cout << best << endl;
    return 0;
}
