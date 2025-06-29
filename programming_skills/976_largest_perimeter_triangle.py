class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return next(
            (
                nums[i] + nums[i + 1] + nums[i + 2]
                for i in range(len(nums) - 2)
                if nums[i] < nums[i + 1] + nums[i + 2]
            ),
            0,
        )


if __name__ == "__main__":
    nums = [2, 1, 2]
    solution = Solution()
    print(solution.largestPerimeter(nums))

    nums = [1, 2, 1, 10]
    solution = Solution()
    print(solution.largestPerimeter(nums))
