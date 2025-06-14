class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)) or (
            all(nums[i] <= nums[i+1] for i in range(len(nums) - 1))
        )


if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    solution = Solution()
    print(solution.isMonotonic(nums))

    nums = [6, 5, 4, 4]
    solution = Solution()
    print(solution.isMonotonic(nums))

    nums = [1, 3, 2]
    solution = Solution()
    print(solution.isMonotonic(nums))
