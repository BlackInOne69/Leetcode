# Last updated: 1/9/2026, 11:45:52 PM
from math import gcd

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        max_points = 0

        for i in range(len(points)):
            slopes = {}
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Vertical line
                if dx == 0:
                    slope = (1, 0)

                # Horizontal line
                elif dy == 0:
                    slope = (0, 1)

                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # Normalize sign
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

            # +1 for the base point itself
            current_max = 1
            if slopes:
                current_max += max(slopes.values())

            max_points = max(max_points, current_max)

        return max_points
