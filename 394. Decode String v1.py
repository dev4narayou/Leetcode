import unittest


# my own solution
# there are optimisation to be made, it's good but not the best




class Solution:
    # flattens nested arrays
    def flatten(self, nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result

    def decodeString(self, s: str) -> str:
        return ''.join(self.detectPortion(s, 0))

    # detects the portion of the string that needs to be repeated
    # and sends it to decodePortion to be decoded
    def detectPortion(self, s: str, start):
        res = []
        i = 0

        while True:
            if i >= len(s):
                break

            if s[i].isdigit():
                repeats = []
                # detect if there are multiple digits
                while s[i].isdigit():
                    repeats.append(s[i])
                    i += 1

                repeats = int(''.join(repeats))

                start = i
                end = i
                stack = []
                for j in range(i, len(s)):
                    if s[j] == '[':
                        stack.append(s[j])
                    elif s[j] == ']':
                        stack.pop()
                    if not stack:
                        end = j
                        break
                res.append(self.decodePortion(s[start:end+1], repeats))
                i = end + 1

            else:
                res.append(s[i])
                i += 1

        return self.flatten(res)

    # decodes the portion of the string that needs to be repeated
    def decodePortion(self, s, repeats):
        return repeats * self.detectPortion(s[1:-1], 0)






if __name__ == '__main__':
    # s = 'abc3[def]ghi'
    # s = '3[a2[c]]'
    # s = "3[a]2[bc]" # Expected: 'aaabcbc'
    s = "100[leetcode]"
    start = 3
    sol = Solution()
    print(sol.decodeString(s))




# class TestDecodeString(unittest.TestCase):
#     def test_decodeString(self):
#         s = '3[a]2[bc]'
#         self.assertEqual(Solution().decodeString(s), 'aaabcbc')

#     def test_decodeString_nested(self):
#         s = '3[a2[c]]'
#         self.assertEqual(Solution().decodeString(s), 'accaccacc')

#     def test_decodeString_multiple(self):
#         s = '2[abc]3[cd]ef'
#         self.assertEqual(Solution().decodeString(s), 'abcabccdcdcdef')

#     def test_decodeString_empty_string(self):
#         s = ''
#         self.assertEqual(Solution().decodeString(s), '')

#     def test_decodeString_no_repeats(self):
#         s = 'abc[def]ghi'
#         self.assertEqual(Solution().decodeString(s), 'abc[def]ghi')

# if __name__ == '__main__':
#     unittest.main()
