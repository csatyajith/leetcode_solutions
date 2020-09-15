class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split(".")
        s2 = version2.split(".")
        i = 0
        while i < (min(len(s1), len(s2))):
            if int(s1[i]) < int(s2[i]):
                return -1
            if int(s1[i]) > int(s2[i]):
                return 1
            i += 1
        if i < len(s1):
            for j in range(i, len(s1)):
                if int(s1[j]) > 0:
                    return 1
        if i < len(s2):
            for j in range(i, len(s2)):
                if int(s2[j]) > 0:
                    return 1

        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.compareVersion("7.2.5.3", "7.2.6"))
