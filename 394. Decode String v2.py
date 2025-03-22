class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr_chars = []

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append(("".join(curr_chars), num))  # store string and repeat count
                curr_chars, num = [], 0
            elif char == ']':
                last_str, repeat = stack.pop()
                curr_chars = list(last_str) + curr_chars * repeat
            else:
                curr_chars.append(char)

        return "".join(curr_chars)


if __name__ == '__main__':
    # s = 'abc3[def]ghi'
    s = '3[a2[c]]'
    # s = "3[a]2[bc]" # Expected: 'aaabcbc'
    # s = "100[leetcode]"
    start = 3
    sol = Solution()
    print(sol.decodeString(s))
