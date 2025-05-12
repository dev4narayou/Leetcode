# most optimised solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        max_subarray = nums[0]
        current_sum = nums[0]

        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])

            max_subarray = max(max_subarray, current_sum)

        return max_subarray


# refined DP:
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)

#         dp = [0] * n
#         dp[0] = nums[0]

#         max_subarray = dp[0]

#         # for each i, dp[i] = max(starting new subarray on i, previous best subarray ending i-1 + i)
#         for i in range(1, n):
#             dp[i] = max(nums[i], dp[i-1] + nums[i])
#             max_subarray = max(max_subarray, dp[i])

#         return max_subarray

## early attempt:
## not optimal, but works for some test cases
# times out
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = nums[0]

#         for i in range(0, n):
#             dp[i] = nums[i] # before calculating optimality, pre-populate w/ default value
#             max_subarray = dp[i]
#             # first compare all the sums of valid subarrays including nums[i]
#             # j represents the range
#             # the subarrays are growing progressively l to r
#             sum = 0
#             for j in range(0, i+1):
#                 sum += nums[i-j]
#                 max_subarray = max(max_subarray, sum)

#             # next, check all the previous best subarray values stored in dp
#             for j in range(0, i+1):
#                 max_subarray = max(dp[j], max_subarray)

#             # persist best max subarray value for this iteration
#             dp[i] = max_subarray

#             # print(f'dp at {i}th iteration is {dp}')

#         # dp[n] represents the optimal subarray length for list nums of length n
#         return dp[n-1]


