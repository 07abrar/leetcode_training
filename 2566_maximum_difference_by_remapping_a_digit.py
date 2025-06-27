class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 9
        num_str = str(num)
        if all(i == "9" for i in num_str):
            return num

        max_num, min_num = None, None
        for i, num in enumerate(num_str):
            if max_num is None and num != "9":
                first_num = num
                max_num = num_str.replace(first_num, '9')
            if min_num is None and num != "0":
                first_num = num
                min_num = num_str.replace(first_num, '0')
            if max_num and min_num:
                break
            if i == len(num_str) - 1:
                return max(max_num, num)
        return int(max_num) - int(min_num)


if __name__ == "__main__":
    nums = 11891
    solution = Solution()
    print(solution.minMaxDifference(nums))

    nums = 90
    solution = Solution()
    print(solution.minMaxDifference(nums))

    nums = 99999
    solution = Solution()
    print(solution.minMaxDifference(nums))

    nums = 0
    solution = Solution()
    print(solution.minMaxDifference(nums))
