class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # Iterate until half length.
        for i in range(1, (int(len(s) / 2)+1)):
            # Check if i is a factor of len(s). If not, skip i.
            if len(s) % i != 0:
                continue

            sub_strings = []
            k = 0

            # Else, split s into len(s)/i parts of length i each.
            while k < len(s):
                sub_strings.append(s[k:k+i])
                k = k+i

            # if all elements are equal, return false.
            if sub_strings.count(sub_strings[0]) == len(sub_strings):
                return True

        # if nothing is returned above, return true
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))
    print(sol.repeatedSubstringPattern("aba"))
    print(sol.repeatedSubstringPattern("aa"))
