from typing import List


class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        sum_elements = sum(nums)
        modulo_nums = sum_elements % p
        i = 0
        j = 1
        total_len = len(nums)
        curr_len = 0
        while j<len(nums):
            if sum(nums[i:j]) % p == modulo_nums:
                if curr_len < total_len



if __name__ == '__main__':
    sol = Solution()
    assert sol.minSubarray(nums=[3, 1, 4, 2], p=6) == 1
    assert sol.minSubarray(nums=[6, 3, 5, 2], p=9) == 2
    assert sol.minSubarray(nums=[1, 2, 3], p=3) == 0
    assert sol.minSubarray(nums=[1, 2, 3], p=7) == -1
    assert sol.minSubarray(nums=[1000000000, 1000000000, 1000000000], p=3) == 0
