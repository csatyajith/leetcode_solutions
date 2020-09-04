class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, (int(len(s) / 2)+1)):
            sub_strings = []
            k = 0
            while k < len(s):
                sub_strings.append(s[k:k+i])
                k = k+i
            if sub_strings.count(sub_strings[0]) == len(sub_strings):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))
    print(sol.repeatedSubstringPattern("aba"))
    print(sol.repeatedSubstringPattern("aa"))
