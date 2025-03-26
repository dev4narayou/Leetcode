from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placeable = 0
        left_ok = True
        for i in range(len(flowerbed)-1):
            if flowerbed[i] == 1:
                left_ok = False
                continue
            else:
                if left_ok and flowerbed[i+1] == 0:
                    placeable += 1
                    left_ok = False
                else:
                    left_ok = True

        if left_ok and flowerbed[-1] == 0:
            placeable += 1

        return placeable >= n

# Cleaner Solution:
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         count = 0
#         i = 0
#         while i < len(flowerbed):
#             if (flowerbed[i] == 0 and
#                 (i == 0 or flowerbed[i - 1] == 0) and
#                 (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
#                 flowerbed[i] = 1
#                 count += 1
#                 i += 2  # skip the next spot
#             else:
#                 i += 1
#         return count >= n


if __name__ == "__main__":
    sol = Solution()
    flowerbed1 = [1,0,0,0,1,0,0]
    n1 = 2
    print(sol.canPlaceFlowers(flowerbed1, n1))
