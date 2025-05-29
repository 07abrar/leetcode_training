class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        # indices = []
        # indices.extend(i for i, word in enumerate(words) if x in word)
        # return indices
        return [i for i, word in enumerate(words) if x in word]

if __name__ == "__main__":
    words = ["leet","code"]
    x = "e"
    solution = Solution()
    print(solution.findWordsContaining(words,x))

    words = ["abc","bcd","aaaa","cbc"]
    x = "z"
    solution = Solution()
    print(solution.findWordsContaining(words,x))