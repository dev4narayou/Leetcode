class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            # odd
            l1, r1 = self.expandFromCenter(s, i, i)
            # even
            l2, r2 = self.expandFromCenter(s, i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j, s):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1, j - i - 1  # return start, end, and length

        longest = 0
        start, end = 0, 0

        for i in range(len(s)):
            # odd-length center
            l1, r1, len1 = expand(i, i, s)
            if len1 > longest:
                longest = len1
                start, end = l1, r1

            # even-length center
            l2, r2, len2 = expand(i, i + 1, s)
            if len2 > longest:
                longest = len2
                start, end = l2, r2

        return s[start:end + 1]