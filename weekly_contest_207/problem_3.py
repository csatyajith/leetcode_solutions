from typing import List


class Solution:

    def get_max_neighbor(self, grid, pos):
        neighbor_pos = [[pos[0] + 1, pos[1]], [pos[0] - 1, pos[1]], [pos[0], pos[1] + 1], [pos[0], pos[1] - 1]]
        max_neighbor = None
        max_neighbor_val = -5
        for p in neighbor_pos:
            if 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0]):
                if grid[p[0]][p[1]] is not None and grid[p[0]][p[1]] > max_neighbor_val:
                    max_neighbor = p
                    max_neighbor_val = grid[p[0]][p[1]]
        return max_neighbor

    def maxProductPath(self, grid: List[List[int]]) -> int:
        pos = [0, 0]
        path = []
        while pos[0] < len(grid) or pos[1] < len(grid[0]):
            max_neighbor = self.get_max_neighbor(grid, pos)
            if max_neighbor is not None:



if __name__ == '__main__':
    sol = Solution()
