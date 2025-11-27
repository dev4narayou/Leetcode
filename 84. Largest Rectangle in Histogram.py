# O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_a = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                w = i - j
                a = h * w
                max_a = max(max_a, a)
                start = j
            stack.append((height, start))

        while stack:
            h, j = stack.pop()
            w = n - j
            max_a = max(max_a, h * w)

        return max_a


# NAIVE: too slow
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        dp = [0 for _ in range(len(heights))]
        dp[0] = heights[0]
        for i in range(1, len(heights)):
            # options are
            # 1. take dp[i-1]
            # 2. take new rect made from single current height
            # 3. take new rectange made from min height combination of a range
            # need to iterate backwards (naive)

            max_area = heights[i]  # init with just taking the current height rectangle
            new_rect = heights[i]
            for j in range(i - 1, -1, -1):
                new_rect = (i - j + 1) * min(heights[j : i + 1])
                max_area = max(max_area, new_rect)

            max_area = max(max_area, dp[i - 1])
            dp[i] = max_area

        return dp[-1]
