class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        for s in operations:
            try:
                score.append(int(s))
            except ValueError:
                if s == "+":
                    sum_last_two = score[-2] + score[-1]
                    score.append(sum_last_two)
                elif s == "C":
                    score.pop()
                elif s == "D":
                    double_previous = score[-1] * 2
                    score.append(double_previous)
        return sum(score)


if __name__ == "__main__":
    s = ["5", "2", "C", "D", "+"]
    solution = Solution()
    print(solution.calPoints(s))

    s = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    solution = Solution()
    print(solution.calPoints(s))

    s = ["1", "C"]
    solution = Solution()
    print(solution.calPoints(s))
