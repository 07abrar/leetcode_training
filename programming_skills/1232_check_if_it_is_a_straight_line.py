class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        coordinates.sort(key=lambda x: x[0])
        try:
            m = ((coordinates[1][1] - coordinates[0][1]) /
                 (coordinates[1][0] - coordinates[0][0]))
        except ZeroDivisionError:
            m = float('inf')
        for i in range(len(coordinates) - 1):
            try:
                m1 = ((coordinates[i+1][1] - coordinates[i][1]) /
                      (coordinates[i+1][0] - coordinates[i][0]))
            except ZeroDivisionError:
                m1 = float('inf')
            if m1 != m:
                return False
        return True


if __name__ == "__main__":
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    solution = Solution()
    print(solution.checkStraightLine(coordinates))

    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    solution = Solution()
    print(solution.checkStraightLine(coordinates))
