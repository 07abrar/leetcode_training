class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1, res2 = 0, 0
        for d in num1:
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))
        return str(res1 * res2)


if __name__ == "__main__":
    num1, num2 = "2", "3"  # Fix: Use tuple unpacking
    solution = Solution()
    print(solution.multiply(num1, num2))

    num1, num2 = "123", "456"  # Fix: Use tuple unpacking
    solution = Solution()
    print(solution.multiply(num1, num2))
