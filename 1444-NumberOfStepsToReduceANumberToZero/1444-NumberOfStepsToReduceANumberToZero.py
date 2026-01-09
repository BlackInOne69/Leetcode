# Last updated: 1/9/2026, 11:45:45 PM
class Solution:
    def numberOfSteps(self, num):
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            steps += 1
        return steps