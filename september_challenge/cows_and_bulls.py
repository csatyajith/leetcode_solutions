class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        result = {"A": 0, "B": 0}
        s_counts = {str(x): 0 for x in range(10)}
        g_counts = {str(x): 0 for x in range(10)}
        for i, c in enumerate(guess):
            if c == secret[i]:
                result["A"] += 1
            else:
                g_counts[c] += 1
                s_counts[secret[i]] += 1
        for i in s_counts.keys():
            result["B"] += min(s_counts[i], g_counts[i])
        return "{}A{}B".format(result["A"], result["B"])


if __name__ == '__main__':
    sol = Solution()
    assert sol.getHint("1807", "7810") == "1A3B"
