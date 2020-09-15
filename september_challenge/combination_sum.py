from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from itertools import combinations
        coms = []
        nums = list(range(1, 10))
        for c in combinations(nums, k):
            if sum(c) == n:
                coms.append(list(c))

        return coms


if __name__ == '__main__':
    sol = Solution()
    assert sol.combinationSum3(k=3, n=7) == [[1, 2, 4]]
