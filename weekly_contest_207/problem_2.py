class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sub_strings = []
        sub_strings_1 = []
        reversed_s = s[::-1]
        i = 0
        j = 1
        while True:
            if reversed_s[i:j] not in sub_strings:
                sub_strings.append(reversed_s[i:j])
                i = j
                j = j + 1
            else:
                j += 1
            if j > len(s):
                break
        i = 0
        j = 1
        while True:
            if s[i:j] not in sub_strings_1:
                if j < len(s) - 1 and s[j] == s[j + 1]:
                    j += 1
                else:
                    sub_strings_1.append(s[i:j])
                    i = j
                    j = j + 1
            else:
                j += 1
            if j >= len(s):
                break

        return max(len(sub_strings), len(sub_strings_1))


if __name__ == '__main__':
    sol = Solution()
    # assert sol.maxUniqueSplit("ababccc") == 5
    # assert sol.maxUniqueSplit("aba") == 2
    # assert sol.maxUniqueSplit("aa") == 1
    # assert sol.maxUniqueSplit("addbsd") == 5
    # assert sol.maxUniqueSplit("hmadataa") == 6
    assert sol.maxUniqueSplit("gpaccacseleac") == 10
