from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if sorted(arr) == arr:
            return 0
        i = 0
        j = len(arr) - 1
        shortest = len(arr) - 1
        while i < j:
            a1 = arr[0:i]
            a1.extend(arr[j:])
            if sorted(a1) == a1:
                shortest = j - i
            else:
                if arr[j-1]
        return shortest


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
    print(sol.findLengthOfShortestSubarray([5, 4, 3, 2, 1]))
    print(sol.findLengthOfShortestSubarray([1, 2, 3]))
    print(sol.findLengthOfShortestSubarray([1]))
    print(sol.findLengthOfShortestSubarray([6, 3, 10, 11, 15, 20, 13, 3, 18, 12]))
    print(sol.findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1]))
    print(sol.findLengthOfShortestSubarray([10, 13, 17, 21, 15, 15, 9, 17, 22, 22, 13]))
