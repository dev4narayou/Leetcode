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


if __name__ == "__main__":
    sol = Solution()
    flowerbed1 = [1,0,0,0,1,0,0]
    n1 = 2
    print(sol.canPlaceFlowers(flowerbed1, n1)) 
