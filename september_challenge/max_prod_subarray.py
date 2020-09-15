from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev_nums = nums[::-1]

        for i in range(1, len(nums)):
            if nums[i - 1] != 0:
                nums[i] *= nums[i - 1]
            if rev_nums[i - 1] != 0:
                rev_nums[i] *= rev_nums[i - 1]

        nums.extend(rev_nums)
        return max(nums)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([-2, 0, -3, -4, -5]))
