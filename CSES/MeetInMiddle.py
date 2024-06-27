# You are given an array of n numbers. 
# In how many ways can you choose a subset of the numbers with sum x?
import bisect
n , x = map(int,input().split())
nums = list(map(int,input().split()))

def get_subset_sum(arr):
  res =[]
  n = len(arr)
  for mask in range(1<<n):
    s = 0
    for j in range(n):
      if mask & 1<<j:
        s+=arr[j]
    res.append(s)
  return sorted(res)

left = get_subset_sum(nums[:n//2])
right = get_subset_sum(nums[n//2:])
ans = 0
for ele in left:
  idx1 = bisect.bisect_left(right,x - ele)
  idx2 = bisect.bisect_right(right,x-ele)
  ans+= idx2-idx1
print(ans)