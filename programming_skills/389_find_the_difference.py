class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        try:
            return (set(t) - set(s)).pop()
        except KeyError:
            s = list(s)
            t = list(t)
            for x in s:
                t.remove(x)
            return t.pop()

if __name__ == "__main__":
    s = "a"
    t = "aa"
    solution = Solution()
    print(solution.findTheDifference(s,t))
