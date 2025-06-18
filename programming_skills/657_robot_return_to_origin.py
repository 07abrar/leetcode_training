class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coords = [0, 0]
        for move in moves:
            if move == "U":
                coords[1] += 1
            elif move == "R":
                coords[0] += 1
            elif move == "D":
                coords[1] -= 1
            else:
                coords[0] -= 1
        return coords == [0, 0]


if __name__ == "__main__":
    moves = "UD"
    solution = Solution()
    print(solution.judgeCircle(moves))

    moves = "LL"
    solution = Solution()
    print(solution.judgeCircle(moves))
