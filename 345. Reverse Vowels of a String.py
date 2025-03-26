class Solution:
    def reverseVowels(self, s: str) -> str:
        output = list(s)
        l = 0
        r = len(s)-1
        vowels = set(['a', 'e','i','o','u', 'A', 'E', 'I', 'O', 'U'])

        while l < r:
            if output[l] in vowels:
                if output[r] in vowels:
                    temp = output[l]
                    output[l] = output[r]
                    output[r] = temp
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1

        return ''.join(output)


        