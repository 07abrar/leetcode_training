class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes_row = set()
        zeroes_column = set()
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    zeroes_row.add(i)
                    zeroes_column.add(j)
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in zeroes_row or j in zeroes_column:
                    matrix[i][j] = 0
        return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution = Solution()
    print(solution.setZeroes(matrix))

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution = Solution()
    print(solution.setZeroes(matrix))

    matrix = [[-4, -2147483648, 6, -7, 0],
              [-8, 6, -8, -6, 0], [2147483647, 2, -9, -6, -10]]
    solution = Solution()
    print(solution.setZeroes(matrix))
