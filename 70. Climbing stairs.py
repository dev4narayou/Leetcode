# recursive
# times out
# class Solution:
#     def climbStairs(self, n: int) -> int:

#         def f(n):
#             if n == 0:
#                 return 1
#             elif n == 1:
#                 return 1
#             return f(n-1) + f(n-2)


#         return f(n)




# DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]



if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(f"Number of ways to climb {n} stairs: {sol.climbStairs(n)}")