# Last updated: 1/9/2026, 11:45:43 PM
class Solution:
    def longestPalindrome(self, s):
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        length = 0
        odd_found = False
        for freq in count.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True

        if odd_found:
            length += 1

        return length
