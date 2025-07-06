class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dinamic_list = [0] * (n + 1)
            dinamic_list[0] = 0
            dinamic_list[1] = 1
            for i in range(2, n+1):
                dinamic_list[i] = dinamic_list[i-1] + dinamic_list[i-2]
            return dinamic_list[-1]


if __name__ == "__main__":
    n = 2
    solution = Solution()
    print(solution.fib(n))

    n = 3
    solution = Solution()
    print(solution.fib(n))

    n = 4
    solution = Solution()
    print(solution.fib(n))
