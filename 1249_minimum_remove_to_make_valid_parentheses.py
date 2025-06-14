class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        indices_to_remove = set()
        parenthese_list = []
        for i, char in enumerate(s):
            if char == "(":
                parenthese_list.append((i, char))
            elif char == ")":
                if parenthese_list:
                    parenthese_list.pop()
                else:
                    indices_to_remove.add(i)
            else:
                continue
        if parenthese_list:
            for idx, _ in parenthese_list:
                indices_to_remove.add(idx)
        word = list(s)
        for i in indices_to_remove:
            word[i] = ""
        return "".join(word)


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    solution = Solution()
    print(solution.minRemoveToMakeValid(s))

    s = "a)b(c)d"
    solution = Solution()
    print(solution.minRemoveToMakeValid(s))

    s = "))(("
    solution = Solution()
    print(solution.minRemoveToMakeValid(s))

    s = ")))))"
    solution = Solution()
    print(solution.minRemoveToMakeValid(s))

    s = "())()((("
    solution = Solution()
    print(solution.minRemoveToMakeValid(s))
