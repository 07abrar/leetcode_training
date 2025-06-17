class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(d) for d in str(num)]
        max_digits = digits.copy()
        min_digits = digits.copy()
        first_non_nine_digit = digits[next(
            (i for i in range(len(digits)) if digits[i] != 9), 0
        )]
        first_non_one_indice = next(
            (i for i in range(len(digits)) if digits[i] != 1), 0
        )
        if first_non_one_indice != 0:
            i_start = 1
            while True:
                first_minimum_digit = digits[next(
                    (i for i in range(first_non_one_indice, len(digits))
                     if digits[i] != 0), i_start
                )]
                if first_minimum_digit != digits[0]:
                    break
                i_start += 1
                first_non_one_indice += 1

        else:
            first_minimum_digit = digits[first_non_one_indice]

        for i, digit in enumerate(digits):
            if digit == first_non_nine_digit:
                max_digits[i] = 9
            if digit == first_minimum_digit:
                min_digits[i] = 1 if first_non_one_indice == 0 else 0
        max_number = int(''.join(str(d) for d in max_digits))
        min_number = int(''.join(str(d) for d in min_digits))
        return max_number - min_number


if __name__ == "__main__":
    nums = 555
    solution = Solution()
    print(solution.maxDiff(nums))

    nums = 9
    solution = Solution()
    print(solution.maxDiff(nums))

    nums = 123456
    solution = Solution()
    print(solution.maxDiff(nums))

    nums = 10000
    solution = Solution()
    print(solution.maxDiff(nums))

    nums = 1101057
    solution = Solution()
    print(solution.maxDiff(nums))
