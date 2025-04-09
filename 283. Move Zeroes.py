from typing import List

# optimised version
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0

        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0


# initial attempt
# uses extra space (which is not desired)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Assumption
        # - don't need to save actual '0' objects, can just transfer values to end

        # can keep track of zero positions
        # after iterating array once, manually place all non-zero values left to right in array
        # then: add zeroes to end

        zero_indices = set()

        # ge zero positions
        for i, num in enumerate(nums):
            if num == 0:
                zero_indices.add(i)

        # add non-zeros left to right into array contiguously
        write = 0 # write pointer
        for i in range(len(nums)):
            if i not in zero_indices:
                nums[write] = nums[i]
                write += 1

        # manually add zeros
        for i in range(len(zero_indices)):
            nums[write] = 0
            write += 1

