from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        spl = 0
        cols = list(map(list, zip(*mat)))
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    if mat[i].count(1) == 1 and cols[j].count(1) == 1:
                        spl += 1
        return spl


if __name__ == '__main__':
    sol = Solution()
    assert sol.numSpecial([[1, 0, 0],
                           [0, 0, 1],
                           [1, 0, 0]]) == 1

    assert sol.numSpecial([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]]) == 3

    assert sol.numSpecial([[0, 0, 0, 1],
                           [1, 0, 0, 0],
                           [0, 1, 1, 0],
                           [0, 0, 0, 0]]) == 2

    assert sol.numSpecial([[0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 1]]) == 3
