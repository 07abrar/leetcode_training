class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
        s=list(s)
        substring = []
        for i, letter in enumerate(s):
            substring.append(letter)
            j = 0
            while True:
                end_idx = (i+1)*(j+1)
                if end_idx > len(s):
                    return False
                if substring != s[(i+1)*j:end_idx]:
                    break
                j += 1
                if end_idx == len(s):
                    return j > 1
        return False

if __name__ == "__main__":
    s = "abab"
    solution = Solution()
    print(solution.repeatedSubstringPattern(s))

    s = "aba"
    solution = Solution()
    print(solution.repeatedSubstringPattern(s))

    s = "abcabcabcabc"
    solution = Solution()
    print(solution.repeatedSubstringPattern(s))