class Solution:
    def modifyString(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        mod_s = ""
        for i, c in enumerate(s):
            if c != "?":
                mod_s += c
                continue
            prior = mod_s[i - 1] if i > 0 else None
            later = s[i + 1] if i < len(s) - 1 else None
            for a in alphabet:
                if a not in [prior, later]:
                    mod_s += a
                    break
        return mod_s


if __name__ == '__main__':
    sol = Solution()
    print(sol.modifyString("?zs"))
    print(sol.modifyString("ubv?w"))
    print(sol.modifyString("j?qg??b"))
    print(sol.modifyString("??yw?ipkj?"))
