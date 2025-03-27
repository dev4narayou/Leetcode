# combines prefix and suffix sums through 2 passes of array
# naturally considers '0' cases
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


# not efficient
# import operator
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prod = 1
#         for i in range(len(nums)):
#             if nums[i]:
#                 prod = prod * nums[i]

#         num_zeros = nums.count(0)
#         if num_zeros > 1:
#             return [0] * len(nums)

#         if num_zeros == 1:
#             return [0 if nums[i] else prod for i in range(len(nums))]

#         else:
#             return [prod // nums[i] for i in range(len(nums))]



