class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        face = 0   # north, west, south, east = 0, 1, 2, 3
        position = [0, 0]
        for move in instructions:
            if move == "G":
                if face == 0:
                    position[1] += 1
                elif face == 1:
                    position[0] -= 1
                elif face == 2:
                    position[1] -= 1
                else:
                    position[0] += 1
            elif move == "L":
                face += 1
                face %= 4
            else:
                face -= 1
                face %= 4
        return face != 0 or position == [0, 0]


if __name__ == "__main__":
    instructions = "GGLLGG"
    solution = Solution()
    print(solution.isRobotBounded(instructions))

    instructions = "GG"
    solution = Solution()
    print(solution.isRobotBounded(instructions))

    instructions = "GL"
    solution = Solution()
    print(solution.isRobotBounded(instructions))

    instructions = "GLRLLGLL"
    solution = Solution()
    print(solution.isRobotBounded(instructions))
