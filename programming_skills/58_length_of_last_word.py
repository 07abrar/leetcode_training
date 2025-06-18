class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_of_word = []
        word = []
        for i, char in enumerate(s):
            if char != " ":
                word.append(char)
            else:
                if word:
                    list_of_word.append(word)
                word = []
            if i == (len(s)-1) and word:
                list_of_word.append(word)
        return len(list_of_word[-1])


if __name__ == "__main__":
    s = "Hello World"
    solution = Solution()
    print(solution.lengthOfLastWord(s))

    s = "   fly me   to   the moon  "
    solution = Solution()
    print(solution.lengthOfLastWord(s))

    s = "luffy is still joyboy"
    solution = Solution()
    print(solution.lengthOfLastWord(s))
