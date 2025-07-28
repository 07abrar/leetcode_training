class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()


if __name__ == "__main__":
    s = "Hello"
    solution = Solution()
    print(solution.toLowerCase(s))

    s = "here"
    solution = Solution()
    print(solution.toLowerCase(s))

    s = "LOVELY"
    solution = Solution()
    print(solution.toLowerCase(s))
