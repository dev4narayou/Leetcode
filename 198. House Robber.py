from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[1], nums[0])

        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n+1):
            if i == n:
                return dp[n-1]
            rob_profit = nums[i] + dp[i-2]
            best_profit = max(rob_profit, dp[i-1])
            dp[i] = best_profit

        

# Basic output tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))  # Output: 4
    print(sol.rob([2, 7, 9, 3, 1]))  # Output: 12