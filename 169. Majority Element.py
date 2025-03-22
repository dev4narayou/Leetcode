class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        unique_values = []
        [unique_values.append(num) for num in nums if num not in unique_values]
        
        cell = [[0 for i in range(len(nums))] for i in range(len(unique_values))]
        
        for i in range(len(unique_values)): # iterate over the unique values
            for j in range(len(nums)): # iterate over the numbers in nums
                if nums[j] == unique_values[i]:
                    cell[i][j] += 1
                else:
                    cell[i][j] = cell[i][j-1]
                    
        majority = 0
        for i in range(len(cell)):
            if cell[i].max > majority:
                majority = unique_values[i]
        
        return majority
            



fds = Solution()
fds.majorityElement([2,2,1,1,1,2,2])