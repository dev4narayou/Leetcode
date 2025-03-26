class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def compute_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        gcd_length = compute_gcd(len(str1), len(str2))
        return str1[:gcd_length]

        
solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
result = solution.gcdOfStrings(str1, str2)
print(result)