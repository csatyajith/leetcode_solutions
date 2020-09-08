class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        p_s_mapping = dict()
        s_p_mapping = dict()
        for i, c in enumerate(pattern):
            if c not in p_s_mapping.keys():
                p_s_mapping[c] = words[i]
            if words[i] not in s_p_mapping:
                s_p_mapping[words[i]] = c
            if p_s_mapping[c] != words[i] or s_p_mapping[words[i]] != c:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern(pattern="abba", str="dog cat cat dog"))
    print(sol.wordPattern(pattern="abba", str="dog cat cat fish"))
    print(sol.wordPattern(pattern="aaaa", str="dog cat cat dog"))
    print(sol.wordPattern(pattern="abba", str="dog dog dog dog"))
