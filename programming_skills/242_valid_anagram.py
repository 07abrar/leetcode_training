class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s=list(s)
        t=list(t)
        ss = {}
        for i in s:
            ss[i] = ss.get(i,0) + 1
        tt = {}
        for i in t:
            tt[i] = tt.get(i,0) + 1
        return ss==tt


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s,t))

    s = "rat"
    t = "car"
    solution = Solution()
    print(solution.isAnagram(s,t))

    s = "aacc"
    t = "ccac"
    solution = Solution()
    print(solution.isAnagram(s,t))