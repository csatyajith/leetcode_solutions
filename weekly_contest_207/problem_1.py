class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        if spaces == 0:
            return text
        split_text = text.split()
        if len(split_text) == 1:
            return split_text[0] + " " * spaces
        space_per_word = spaces // (len(split_text) - 1)

        remaining = spaces % (len(split_text) - 1)
        final_text = ""
        for i, word in enumerate(split_text):
            final_text += word
            final_text = final_text + " " * space_per_word if i < len(split_text) - 1 else final_text + " " * remaining
        return final_text


if __name__ == '__main__':
    sol = Solution()
    assert sol.reorderSpaces("  this   is  a sentence ") == "this   is   a   sentence"
    assert sol.reorderSpaces(text=" practice   makes   perfect") == "practice   makes   perfect "
    assert sol.reorderSpaces("hello   world") == "hello   world"
    assert sol.reorderSpaces("  walks  udp package   into  bar a") == "walks  udp  package  into  bar  a "
    assert sol.reorderSpaces("a") == "a"
    assert sol.reorderSpaces("  hello") == "hello  "
