# v1
# tracks using indices
# may be more efficient (empirically) to actually just store the values
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        i, j = 0, None

        for index, num in enumerate(nums):
            if num < nums[i]:
                i = index
            elif num > nums[i]:
                # found third
                if j is not None and num > nums[j]:
                    return True
                else:
                    j = index
        return False

