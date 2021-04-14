from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(0, len(arr) - i +1):
                total_sum += sum(arr[j:j + i])
        return total_sum


if __name__ == '__main__':
    sol = Solution()
    assert sol.sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58
    assert sol.sumOddLengthSubarrays([1, 2]) == 3
    assert sol.sumOddLengthSubarrays([10, 11, 12]) == 66
