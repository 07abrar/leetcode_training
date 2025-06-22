class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row, col, drow, dcol = 0, 0, 0, 1
        spiral_mat = []

        for _ in range(len(matrix) * len(matrix[0])):
            spiral_mat.append(matrix[row][col])
            matrix[row][col] = None
            if (row + drow >= len(matrix) or
                    col + dcol >= len(matrix[0]) or
                    row + drow < 0 or
                    col + dcol < 0 or
                    matrix[row + drow][col + dcol] is None
                ):
                drow, dcol = dcol, -drow
            row += drow
            col += dcol
        return spiral_mat


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    print(solution.spiralOrder(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    solution = Solution()
    print(solution.spiralOrder(matrix))

    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    solution = Solution()
    print(solution.spiralOrder(matrix))
