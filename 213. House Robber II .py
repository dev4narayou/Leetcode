class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_linear(arr: List[int]) -> int:
            n = len(arr)
            if n == 0: return 0
            if n == 1: return arr[0]
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            return dp[-1]

        # case 1: exclude last house
        case1 = rob_linear(nums[:-1])
        # case 2: exclude first house
        case2 = rob_linear(nums[1:])

        return max(case1, case2)