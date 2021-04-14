class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        truncated = ""
        for w in s.split()[0:k]:
            truncated = truncated + w + " "
        return truncated[0:-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.truncateSentence("Hello how are you contestant", 4))
