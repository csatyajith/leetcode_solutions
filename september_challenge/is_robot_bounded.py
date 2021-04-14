class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = (0, 0)
        direction = (0, 1)
        direction_movement = {
            (0, 1): {"L": (-1, 0), "R": (1, 0)},
            (1, 0): {"L": (0, 1), "R": (0, -1)},
            (0, -1): {"L": (1, 0), "R": (-1, 0)},
            (-1, 0): {"L": (0, -1), "R": (0, 1)}
        }
        for _ in range(4):
            for i in instructions:
                if i == "G":
                    pos = tuple((pos[k] + direction[k] for k in range(len(direction))))
                else:
                    direction = direction_movement[direction][i]

            if pos == (0, 0):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.isRobotBounded("GGLLGG") is True
    assert sol.isRobotBounded("GG") is False
    assert sol.isRobotBounded("GL") is True
