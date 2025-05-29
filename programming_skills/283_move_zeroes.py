class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_list = [i for i,num in enumerate(nums) if num != 0]
        if not non_zero_list:
            return nums
        for i, idx in enumerate(non_zero_list):
            if i != idx:
                nums[i], nums[idx] = nums[idx], nums[i]
        return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    solution = Solution()
    print(solution.moveZeroes(nums))

    nums = [0]
    solution = Solution()
    print(solution.moveZeroes(nums))

    nums = [0,0,1]
    solution = Solution()
    print(solution.moveZeroes(nums))