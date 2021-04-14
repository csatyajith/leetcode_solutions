from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0 for _ in range(k)]
        mins = {}
        for log in logs:
            if log[0] not in mins:
                mins[log[0]] = []
            mins[log[0]].append(log[1])
        for x in mins:
            k = len(set(mins[x]))
            answer[k - 1] += 1
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.findingUsersActiveMinutes(logs=[[1, 1], [2, 2], [2, 3]], k=4))
