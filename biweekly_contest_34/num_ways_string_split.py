class Solution:
    def numWays(self, s: str) -> int:
        n_ones = s.count("1")
        if n_ones == 0:
            return int(((len(s) - 1) * (len(s) - 2)) / 2) % 1000000007
        if n_ones % 3 != 0:
            return 0
        one_indices = []
        for i, c in enumerate(s):
            if c == "1":
                one_indices.append(i)
        p1 = s[0:one_indices[int((len(one_indices) / 3))]]
        p2 = s[one_indices[int((len(one_indices) / 3))]: one_indices[int(((2 * len(one_indices)) / 3))]]
        m1 = 1
        m2 = 1
        for c in p1[::-1]:
            if c == "0":
                m1 += 1
            if c == "1":
                break
        for c in p2[::-1]:
            if c == "0":
                m2 += 1
            if c == "1":
                break

        return (m1 * m2) % 1000000007


if __name__ == '__main__':
    sol = Solution()
    print(sol.numWays("100100010100110"))
