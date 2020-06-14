class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        matches = {"[": "]",
         "{": "}",
         "(": ")"}

        for char in s:
            if char in matches.keys():
                bracket_stack.append(char)
            elif char in matches.values():
                if len(bracket_stack) == 0:
                    return False
                if matches[bracket_stack[-1]] != char:
                    return False
                bracket_stack.pop()
        if len(bracket_stack) != 0:
            return False
        return True

if __name__ == '__main__':
    print(Solution().isValid("()"))