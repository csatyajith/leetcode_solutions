class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if len(s) == s.count(" ") else len(s.split()[-1])