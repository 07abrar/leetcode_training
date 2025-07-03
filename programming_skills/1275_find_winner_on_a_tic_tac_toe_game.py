class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [[None for _ in range(3)] for _ in range(3)]
        # Fill the board start from A as "X"
        A = True
        for move in moves:
            board[move[0]][move[1]] = "X" if A is True else "O"
            A = not A
        for i in range(3):
            if (
                board[i][0] == board[i][1] == board[i][2] != None
            ):
                return "A" if board[i][0] == "X" else "B"
            if (
                board[0][i] == board[1][i] == board[2][i] != None
            ):
                return "A" if board[0][i] == "X" else "B"
        if (
            board[0][0] == board[1][1] == board[2][2] != None or
            board[2][0] == board[1][1] == board[0][2] != None
        ):
            return "A" if board[1][1] == "X" else "B"
        else:
            return "Pending" if len(moves) < 9 else "Draw"


if __name__ == "__main__":
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    solution = Solution()
    print(solution.tictactoe(moves))

    moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    solution = Solution()
    print(solution.tictactoe(moves))

    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [
        1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    solution = Solution()
    print(solution.tictactoe(moves))

    moves = [[0, 0], [1, 1]]
    solution = Solution()
    print(solution.tictactoe(moves))
