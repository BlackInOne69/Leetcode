# Last updated: 1/31/2026, 8:13:40 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool: # Added 'self'
3        if len(s) != len(t):
4            return False
5        
6        count = {}
7        for char in s:
8            count[char] = count.get(char, 0) + 1
9        
10        for char in t:
11            if char not in count or count[char] == 0:
12                return False
13            count[char] -= 1
14            
15        return True