# Last updated: 1/14/2026, 8:39:53 PM
1class Solution:
2    def integerBreak(self, n: int) -> int:
3        if n == 2:
4            return 1
5        if n == 3:
6            return 2
7
8        product = 1
9        while n > 4:
10            product *= 3
11            n -= 3
12
13        return product * n
14