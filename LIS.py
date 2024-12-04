from bisect import *
N = 10000
# longest increasing subsequnce ending at i
def LIS(nums):
    dp = [10**10]*(N+1)
    lens = [0]*N
    for i,ele in enumerate(nums):
        lens[i] = bisect_left(dp,ele) + 1
        dp[lens[i] - 1] = ele
    return lens

# a[i] > a[j] where i > j
def definitely_increase(nums):
    dp = []
    for num in nums:
        i = bisect.bisect_left(dp, num)
        if 0 <= i < len(dp):
            dp[i] = num
        else:
            dp.append(num)
    return len(dp)

# a[i] >= a[j] where i > j
def definitely_not_reduce(nums):
    dp = []
    for num in nums:
        i = bisect.bisect_right(dp, num)
        if 0 <= i < len(dp):
            dp[i] = num
        else:
            dp.append(num)
    return len(dp)