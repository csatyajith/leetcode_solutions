from typing import List


class Solution:

    def dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        final_cost = 0
        points = [tuple(point) for point in points]
        if len(points) == 1:
            return 0
        tree = [points[0]]
        non_tree = points[1:]
        distances = {}
        sorted_distances = {}
        for i, point1 in enumerate(points):
            for point2 in points[i+1:]:
                distance = self.dist(point1, point2)
                if point1 not in distances:
                    distances[point1] = {}
                if point2 not in distances:
                    distances[point2] = {}
                distances[point1][point2] = distance
                distances[point2][point1] = distance
            sorted_distances[point1] = sorted(distances[point1], key=lambda k: distances[point1][k])

        while len(tree) < len(points):
            min_cost = 10000000
            for t in tree:
                for d in sorted_distances[t]:
                    if d in non_tree:
                        if distances[t][d] < min_cost:
                            min_cost = distances[t][d]
                            min_point = d
                            break
            final_cost += min_cost
            tree.append(min_point)
            non_tree.remove(min_point)
        return final_cost


if __name__ == '__main__':
    sol = Solution()
    assert sol.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert sol.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]) == 18
    assert sol.minCostConnectPoints(points=[[0, 0], [1, 1], [1, 0], [-1, 1]]) == 4
    assert sol.minCostConnectPoints(points=[[-1000000, -1000000], [1000000, 1000000]])
    assert sol.minCostConnectPoints([[0, 0]]) == 0
