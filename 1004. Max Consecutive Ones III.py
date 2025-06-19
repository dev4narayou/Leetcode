from collections import deque
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        q = deque([])
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                q.append(i)
                if len(q) > k:
                    left = q.popleft() + 1

            max_len = max(max_len, i - left + 1)

        return max_len

# NOTES:
"""
    This is a tricky one.
    Key ideas are:
    - Slide window [left..i], enqueue each zero's index in deque.
    - If deque size > k, pop oldest zero and set left = popped_index + 1.
    - After that, update max_len as i - left + 1 on every iteration.
    Just make sure that the invariants and edge cases are handles -> it's easier to have automatic enqueing w/ subsequent checks, rather than splitting that between loops.
"""