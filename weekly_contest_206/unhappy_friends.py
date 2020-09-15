from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairs_dict = {}
        preferences_dict = {}
        unhappy = set()
        for pair in pairs:
            pairs_dict[pair[0]] = pair[1]
            pairs_dict[pair[1]] = pair[0]
        for i, preference in enumerate(preferences):
            preferences_dict[i] = preferences[i]

        for pair in pairs:
            for ele in pair:
                if ele in unhappy:
                    continue
                partner_pref = preferences_dict[ele].index(pairs_dict[ele])
                for i in range(partner_pref):
                    pref_partner = preferences_dict[ele][i]
                    if preferences_dict[pref_partner].index(ele) < preferences_dict[pref_partner].index(
                            pairs_dict[pref_partner]):
                        unhappy.add(ele)
                        unhappy.add(pref_partner)

        return len(unhappy)

if __name__ == '__main__':
    sol = Solution()
    # assert sol.unhappyFriends(n=4, preferences=[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]],
    #                           pairs=[[0, 1], [2, 3]]) == 2
    # assert sol.unhappyFriends(n=2, preferences=[[1], [0]], pairs=[[1, 0]]) == 0
    assert sol.unhappyFriends(n=4, preferences=[[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]],
                              pairs=[[1, 3], [0, 2]]) == 4
