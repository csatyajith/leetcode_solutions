from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total_cost = 0
        i = 0
        j = 1
        while j < len(s):
            if s[i] == s[j]:
                if cost[i] <= cost[j]:
                    total_cost = total_cost + cost[i]

                    i = j
                    j = i + 1
                else:
                    total_cost = total_cost + cost[j]
                    j += 1
            else:
                i = j
                j = i + 1
        return total_cost


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCost(s="abaac", cost=[1, 2, 3, 4, 5]))
    print(sol.minCost(s="abc", cost=[1, 2, 3]))
    print(sol.minCost(s="aabaa", cost=[1, 2, 3, 4, 1]))
    print(sol.minCost("aaaaaaaaaaaaaa", [1, 3, 6, 5, 4, 5, 4, 4, 2, 8, 3, 10, 6, 6]))
