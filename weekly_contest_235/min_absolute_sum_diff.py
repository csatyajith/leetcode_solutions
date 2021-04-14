from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diffs = [abs(nums1[x] - nums2[x]) for x in range(n)]
        min_diff = sum(diffs)

        uniques_n1 = list(set(nums1))
        max_diffs_indices = []

        new_error = 100000000
        max_saving = 0
        best_index = 0
        for k in range(len(diffs)):
            for n1 in uniques_n1:
                if abs(n1 - nums2[k]) < new_error:
                    new_error = abs(n1 - nums2[k])
                    if diffs[k] - new_error > max_saving:
                        best_index = k
                        max_saving = diffs[k] - new_error
        return (min_diff - (diffs[best_index] - abs(nums1[best_index] - nums2[best_index]))) % 1000000007


if __name__ == '__main__':
    sol = Solution()
    print(sol.minAbsoluteSumDiff(nums1=[1, 7, 5], nums2=[2, 3, 5]))
    print(sol.minAbsoluteSumDiff(nums1=[2, 4, 6, 8, 10], nums2=[2, 4, 6, 8, 10]))
    print(sol.minAbsoluteSumDiff(nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
