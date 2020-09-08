from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_diag = 0
        for i, l in enumerate(mat):
            sum_diag += l[i]
            if len(l) % 2 == 1 and i == ((len(l)-1) / 2):
                continue
            sum_diag += l[-(i+1)]
        return sum_diag


if __name__ == '__main__':
    sol = Solution()
    print(sol.diagonalSum([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]]))
    print(sol.diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))
    print(sol.diagonalSum([[5]]))
    print(sol.diagonalSum([[]]))