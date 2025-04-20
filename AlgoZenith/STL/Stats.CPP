#include<bits/stdc++.h>
using namespace std;

struct data_dashboard
{
    // mean
    int sum = 0;
    int cnt = 0;
    // variance
    int sumsq = 0;

    // mode
    map<int, int> freq;
    multiset<pair<int, int>> freq_order;

    // median
    multiset<int> low, high;

    void balance()
    {
        while (low.size() < high.size())
        {
            int x = *high.begin();
            high.erase(high.find(x));
            low.insert(x);
        }
        while (low.size() > high.size() + 1)
        {
            int x = *low.rbegin();
            low.erase(low.find(x));
            high.insert(x);
        }
    }

    void insert(int x)
    {
        cnt++;
        sum += x;
        sumsq += x * x;

        // mode
        if (freq_order.find(make_pair(freq[x], x)) != freq_order.end())
        {
            freq_order.erase(freq_order.find(make_pair(freq[x], x)));
        }
        freq[x]++;
        freq_order.insert(make_pair(freq[x], x));

        // median
        if (low.empty())
        {
            low.insert(x);
        }
        else if (x <= (*low.rbegin()))
        {
            low.insert(x);
        }
        else
        {
            high.insert(x);
        }
        balance();
    }

    void remove(int x)
    {
        cnt--;
        sum -= x;
        sumsq -= x * x;

        // remove mode
        if (freq_order.find(make_pair(freq[x], x)) != freq_order.end())
        {
            freq_order.erase(freq_order.find(make_pair(freq[x], x)));
        }
        freq[x]--;
        freq_order.insert(make_pair(freq[x], x));

        // median
        if (high.find(x) != high.end())
        {
            high.erase(high.find(x));
        }
        else if (low.find(x) != low.end())
        {
            low.erase(low.find(x));
        }
        balance();
    }

    double mean()
    {
        return sum / cnt;
    }

    double variance()
    {
        return sumsq / cnt - mean() * mean();
    }

    double mode()
    {
        return freq_order.rbegin()->second;
    }

    double median()
    {
        if ((low.size() + high.size()) % 2)
        {
            return *low.rbegin();
        }
        else
        {
            return (*low.rbegin() + (*high.begin())) / 2.0;
        }
    }
};


struct bag{
    multiset<int> left, right;
    int l_sum = 0, r_sum = 0;
    
    // we will rebalance if right.sz == lft.sz + 1 is not the case
    void rebalance(){
        while(right.size() > left.size() + 1){
            // first element of right will be inserted into left.
            auto it = right.begin();
            int val = *it;
            r_sum -= val;
            right.erase(it);
            
            // inserting into the left multiset
            left.insert(val);
            l_sum += val;
        }
        
        while(left.size() > right.size()){
            // last element of the left ms -> right ms
            auto it = prev(left.end());
            int val = *it;
            l_sum -= val;
            left.erase(it);
            
            // inserting into right multiset
            r_sum += val;
            right.insert(val);
        }
    };
    
    // always insert in right multiset and then rebalance()
    void insert(int x){
        if(left.size() == 0 and right.size() == 0){
            right.insert(x);
            r_sum += x;
        }
        
        else{
            if(x >= *right.begin()){
                right.insert(x);
                r_sum += x;
            }else{
                left.insert(x);
                l_sum += x;
            }
        }
        
        rebalance();
    }
    
    
    // check for element in right first to delete and then check for elementin left ms.
    void erase(int x){
       if(right.empty()) return;
       if(x >= *right.begin()){
           if(right.count(x)){
               auto it = right.find(x);
               right.erase(it);
               r_sum -= x;
           }
       }
       else{
           if(left.count(x)){
               auto it = left.find(x);
               left.erase(it);
               l_sum -= x;
           }
       }
       
       rebalance();
    }
    
    
    int get_median(){
        return *right.begin();
    }
    
    int tot_cost(){
        int cost = 0;
        int median = get_median();
        cost += ((left.size()*median) - l_sum);
        cost += (r_sum - (right.size()*median));
        return cost;
    }
};

struct bag2
{
    int K;
    priority_queue<int> pq;
    int sumK;
    void init(int _K)
    {
        K = _K;
        sumK = 0;
    }
    void insert(int x)  // O(logn)
    {
        sumK += x;
        pq.push(-x);
        if (pq.size() > K)
        {
            int sm = -pq.top();
            pq.pop();
            sumK -= sm;
        }
    }

    int topk()   // O(1)
    {
        return sumK;
    }
};


struct bag3
{
    int K;
    multiset<int> mt1, mt2;
    int sumK;

    void init(int _K)
    {
        K = _K;
        sumK = 0;
        mt1.clear();
        mt2.clear();
    }

    void insert(int x)   //O(logn)
    {
        mt1.insert(x);
        sumK += x;
        if (mt1.size() > K)
        {
            auto it = mt1.begin();
            sumK -= *it;
            mt2.insert(*it);
            mt1.erase(it);
        }
    }

    void remove(int x)   //O(logn)
    {
        if (mt1.find(x) != mt1.end())
        {
            mt1.erase(mt1.find(x));
            sumK -= x;
        }
        else if (mt2.find(x) != mt2.end())
        {
            mt2.erase(mt2.find(x));
        }
        if (mt1.size() < K && !mt2.empty())
        {
            auto it = mt2.end();
            it--;
            int val = *it;
            mt2.erase(it);
            mt1.insert(val);
            sumK += val;
        }
    }

    int getSum()
    {
        return sumK;
    }
};
