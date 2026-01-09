# Last updated: 1/9/2026, 11:45:54 PM
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        length = 0

        for word in words:
            if length + len(word) + len(line) > maxWidth:
                spaces = maxWidth - length
                if len(line) == 1:
                    result.append(line[0] + " " * spaces)
                else:
                    gap, extra = divmod(spaces, len(line) - 1)
                    for i in range(extra):
                        line[i] += " "
                    result.append((" " * gap).join(line))
                line = []
                length = 0

            line.append(word)
            length += len(word)

        last = " ".join(line)
        last += " " * (maxWidth - len(last))
        result.append(last)

        return result
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

sol = Solution()
output = sol.fullJustify(words, maxWidth)

for line in output:
    print(f"'{line}'")
  