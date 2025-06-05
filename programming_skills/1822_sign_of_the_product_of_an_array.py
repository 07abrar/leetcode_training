class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums: return 0
        x = 1
        for num in nums:
            x *= num
        return self.signFunc(x)

    def signFunc(self, x):
        return 1 if x > 0 else -1

if __name__ == "__main__":
    nums = [-1,-2,-3,-4,3,2,1]
    solution = Solution()
    print(solution.arraySign(nums))

    nums = [1,5,0,2,-3]
    solution = Solution()
    print(solution.arraySign(nums))

    nums = [-1,1,-1,1,-1]
    solution = Solution()
    print(solution.arraySign(nums))