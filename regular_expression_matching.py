class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        j = len(s) - 1
        i = len(p) - 1
        while True:
            if p[i] == "*":
                while (s[j] == p[i - 1]) or (p[i - 1] == "."):
                    j -= 1
                    if j == -1:
                        break
                i -= 2
            elif p[i] == ".":
                if j == -1:
                    return False
                j -= 1
                i -= 1
            else:
                if j == -1 or s[j] != p[i]:
                    return False
                j -= 1
                i -= 1
            if i < 0:
                break
        if j == -1:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch("aaa", "ab*a*c*a"))
