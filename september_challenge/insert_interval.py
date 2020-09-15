from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = list()
        i = 0
        j = len(intervals) - 1
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                inserted.append(intervals[i])
                i += 1
            else:
                break
        while j >= 0:
            if intervals[j][0] > newInterval[1]:
                inserted.append((intervals[j]))
                j -= 1
            else:
                break

        contiguous = newInterval
        for k in range(i, j + 1):
            contiguous.extend(intervals[k])
        inserted.append([min(contiguous), max(contiguous)])
        return sorted(inserted, key=lambda m: m[0])


if __name__ == '__main__':
    sol = Solution()
    assert sol.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert sol.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) == [[1, 2], [3, 10],
                                                                                                     [12, 16]]
