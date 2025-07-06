class Solution:
    def climbStairs(self, n: int) -> int:
        dinamic_list = [0] * (n + 1)
        dinamic_list[0] = 1
        dinamic_list[1] = 1
        for i in range(2, n+1):
            dinamic_list[i] = dinamic_list[i-1] + dinamic_list[i-2]
        return dinamic_list[-1]


if __name__ == "__main__":
    n = 2
    solution = Solution()
    print(solution.climbStairs(n))

    n = 3
    solution = Solution()
    print(solution.climbStairs(n))

    n = 45
    solution = Solution()
    print(solution.climbStairs(n))
