class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack = list(haystack)
        needle = list(needle)
        number_of_word = len(needle)
        i = 0
        while True:
            if number_of_word+i > len(haystack):
                return -1
            if haystack[i:(number_of_word+i)] == needle[:number_of_word]:
                return i
            i += 1

if __name__ == "__main__":
    s = "sadbutsad"
    t = "sad"
    solution = Solution()
    print(solution.strStr(s,t))

    s = "leetcode"
    t = "leeto"
    solution = Solution()
    print(solution.strStr(s,t))

