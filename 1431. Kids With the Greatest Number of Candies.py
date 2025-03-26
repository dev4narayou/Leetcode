class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [False] * (len(candies))
        for i, candy_amount in enumerate(candies):
            if candy_amount + extraCandies >= max_candies:
                result[i] = True

        return result