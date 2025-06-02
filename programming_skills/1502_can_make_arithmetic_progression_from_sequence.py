class Solution(object):
    def canMakeArithmeticProgression(self, arr: list):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        diff = arr[0] - arr[1]
        return all(arr[i] - arr[i+1] == diff for i in range(len(arr)-1))

if __name__ == "__main__":
    arr = [3,5,1]
    solution = Solution()
    print(solution.canMakeArithmeticProgression(arr))

    arr = [1,2,4]
    solution = Solution()
    print(solution.canMakeArithmeticProgression(arr))