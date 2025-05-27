class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus_one = str(int(''.join(map(str, digits))) + 1)
        return [int(char) for char in plus_one]

if __name__ == "__main__":
    digits = [1,2,3]
    solution = Solution()
    print(solution.plusOne(digits))

    digits = [4,3,2,1]
    solution = Solution()
    print(solution.plusOne(digits))

    digits = [9]
    solution = Solution()
    print(solution.plusOne(digits))