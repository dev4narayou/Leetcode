# class Solution:
#     def tribonacci(self, n: int) -> int:
#         memo = {}
#         return self.trib_aux(n, memo)

#     def trib_aux(self, n, memo):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         elif n in memo:
#             return memo[n]
#         else:
#             res = self.trib_aux(n-1, memo) + self.trib_aux(n-2, memo) + self.trib_aux(n-3, memo)
#             memo[n] = res
#             return res
# exceeds time limit (probs because it recurses top down)

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        for i in range(0, n+1):
            if i == 0:
                memo[i] = 0
            elif i == 1:
                memo[i] = 1
            elif i == 2:
                memo[i] = 1
            else:
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

        return memo[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci(4))  # Output: 4
    print(sol.tribonacci(25)) # Output: 1389537