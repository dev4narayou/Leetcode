"""
Clean Version.
O(N) Time & Space.
Approach: Monotonic Decreasing Stack.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # stores indices
        total_water = 0

        for i, h in enumerate(height):
            # while stack is not empty and current height is taller than top of stack
            while stack and height[stack[-1]] < h:
                bottom_idx = stack.pop()

                # if stack is empty, there is no left wall to hold water
                if not stack:
                    break

                left_idx = stack[-1]

                # calculate dimensions
                # distance between current index and the new top of stack
                width = i - left_idx - 1

                # nounded height: min(left_wall, right_wall) - bottom_height
                bounded_height = min(h, height[left_idx]) - height[bottom_idx]

                total_water += width * bounded_height

            stack.append(i)

        return total_water


"""
This is my first attempt without seeing the solution.
It passes all the tests, however, it seems that memory usage and performance could be improved.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # monotinically decreasing stack
        stack = []  # Tuple: index, height
        max_area = 0

        for i, val in enumerate(height):
            start = i
            while stack and stack[-1][1] < val:
                prev = stack.pop()
                if len(stack) == 0:
                    continue
                min_h = min(val, stack[-1][1])
                trapped = (i - stack[-1][0] - 1) * (min_h - prev[1])
                max_area += trapped
                start = stack[-1][0]

            stack.append((i, val))

        return max_area
