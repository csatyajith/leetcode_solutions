from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        import heapq
        from collections import Counter
        total_sum = 0
        multiplier = Counter()
        for r in requests:
            for x in range(r[0], r[1] + 1):
                multiplier[x] += 1
        sorted_nums = heapq.nlargest(len(multiplier), nums)
        for i, (m, n) in enumerate(multiplier.most_common()):
            total_sum += sorted_nums[i] * n

        return total_sum % ((10**9) + 7)


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxSumRangeQuery([1, 2, 3, 4, 5], [[1, 3], [0, 1]]) == 19
    assert sol.maxSumRangeQuery(nums=[1, 2, 3, 4, 5, 6], requests=[[0, 1]]) == 11
    assert sol.maxSumRangeQuery(nums=[1, 2, 3, 4, 5, 10], requests=[[0, 2], [1, 3], [1, 1]]) == 47
