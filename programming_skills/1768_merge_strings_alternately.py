class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1= list(word1)
        word2= list(word2)
        len1 = len(word1)
        len2 = len(word2)
        minimum = min(len1, len2)
        result = []
        i = 0
        while True:
            result.extend((word1.pop(0), word2.pop(0)))
            i += 1
            if i == minimum:
                break
        if not word1:
            result.extend(word2)
        else:
            result.extend(word1)
        return "".join(result)
