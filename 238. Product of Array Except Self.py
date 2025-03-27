import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in range(len(nums)):
            if nums[i]:
                prod = prod * nums[i]

        num_zeros = nums.count(0)
        if num_zeros > 1:
            return [0] * len(nums)

        if num_zeros == 1:
            return [0 if nums[i] else prod for i in range(len(nums))]

        else:
            return [prod // nums[i] for i in range(len(nums))]


