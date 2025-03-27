from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        output = deque([])
        s = s.split()
        for word in s:
            output.appendleft(word)
            output.appendleft(' ')
        output.popleft()
        return ''.join(output)

if __name__ == "__main__":
    solution = Solution()
    test_string = "the sky is blue"
    print(solution.reverseWords(test_string))