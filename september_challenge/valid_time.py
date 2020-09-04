from itertools import permutations
from typing import List


class Solution:
    def is_valid_time(self, hours, minutes):
        if hours > 23 or minutes > 59:
            return False
        return True

    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = (0, 0)
        if A == [0, 0, 0, 0]:
            return "00:00"
        for p in permutations(A):
            hours = 10 * p[0] + p[1]
            minutes = 10 * p[2] + p[3]

            if self.is_valid_time(hours, minutes):
                if hours > max_time[0]:
                    max_time = (hours, minutes)
                elif hours == max_time[0] and minutes > max_time[1]:
                    max_time = (hours, minutes)

        max_time_str = ""
        if max_time == (0, 0):
            return max_time_str
        else:
            if len(str(max_time[0])) == 1:
                max_time_str += "0"
            max_time_str += str(max_time[0])
            max_time_str += ":"
            if len(str(max_time[1])) == 1:
                max_time_str += "0"

            max_time_str += str(max_time[1])
            return max_time_str


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestTimeFromDigits([0, 0, 0, 0]))
