from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        occurrences = dict()
        for i, c in enumerate(S):
            if c not in occurrences:
                occurrences[c] = []
            occurrences[c].append(i)
        for o in occurrences:
            occurrences[o] = [min(occurrences[o]), max(occurrences[o])]

        partitions = []
        curr_min = 0
        curr_max = 0
        for o in occurrences:
            if occurrences[o][0] > curr_max:
                partitions.append(curr_max)
                curr_min = occurrences[o][0]
            if occurrences[o][0] >= curr_min:
                if occurrences[o][1] > curr_max:
                    curr_max = occurrences[o][1]
        partitions.append(len(S)-1)
        final_partitions = [partitions[0]+1]
        for i, p in enumerate(partitions[1:]):
            final_partitions.append(p - partitions[i])
        return final_partitions


if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
