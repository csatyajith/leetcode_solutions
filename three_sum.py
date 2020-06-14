from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        sol = []
        for i, n in enumerate(sorted_nums):
            if i>0 and n == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                tsum = n + sorted_nums[left] + sorted_nums[right]
                if tsum == 0:
                    sol.append([n, sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif tsum > 0:
                    right -= 1
                else:
                    left += 1
        return sol


if __name__ == '__main__':
    soln = Solution()
    print(soln.threeSum([0,0,0]))
