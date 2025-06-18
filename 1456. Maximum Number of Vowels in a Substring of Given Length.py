class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        n = len(s)
        curr_vowels = max_vowels = sum(1 for char in s[:k] if char in vowels)
        for i in range(1, n-k+1):
            if s[i-1] in vowels:
                curr_vowels -= 1
            if s[i+k-1] in vowels:
                curr_vowels += 1

            if curr_vowels > max_vowels:
                max_vowels = curr_vowels

        return max_vowels

