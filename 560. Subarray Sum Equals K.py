from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # populate sums
        sums = {}
        for i in range(len(nums)):
            sum = nums[i]
            sums[tuple([i, 0])] = sum
            for j in range(i+1, len(nums)):
                sum += nums[j]
                sums[tuple([i, j])] = sum

        count = 0
        for i in range(len(nums)):
            sum = sums[tuple([i, 0])]
            if sum == k:
                count += 1
            for j in range(i+1, len(nums)):
                sum = sums[tuple([i, j])]
                if sum == k:
                    count += 1
                    continue
        return count



