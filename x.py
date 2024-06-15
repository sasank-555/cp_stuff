class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        INF = 10**20
        N = len(nums)
        # def helper(i,cnt,last):
        #     if i==N:
        #         if cnt<=k:
        #             return 0
        #         else:
        #             return -INF
        #     pick = 1+helper(i+1,cnt+int(last!=nums[i]),nums[i])
        #     no = helper(i+1,cnt,last)
        #     return max(pick,no)
        dp = [[[-INF] * (N + 1) for _ in range(k + 2)] for _ in range(N + 1)]

       
        for cnt in range(k + 1):
            for last in range(N + 1):
                dp[N][cnt][last] = 0

        
        for i in range(N - 1, -1, -1):
            for cnt in range(k + 1):
                for last in range(N):
                    new_cnt = cnt + int(nums[i] != nums[last])
                    pick = 1 + dp[i + 1][new_cnt][i] if new_cnt <= k else -INF
                    no_pick = dp[i + 1][cnt][last]
                    dp[i][cnt][last] = max(pick, no_pick)

       
        maxi = -INF
        for i in range(N+1):
            for j in range(k+2):
                for m in range(N+1):
                    maxi = max(maxi,dp[i][j][m])
        return 1+maxi