"""
875. Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""
import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        while l < r:
            # m = (l+r)//2
            m = l + (r - l) // 2
            hours = 0
            for pile in piles:
                # hours += math.ceil(pile/m)
                hours += (pile + m -1)//m
            if hours <= h:
                r = m
            else:
                l = m + 1
        return r

sol = Solution()
piles = [3,6,7,11]
h = 8
piles = [30,11,23,4,20]
h = 5
piles = [30,11,23,4,20]
h = 6
print(sol.minEatingSpeed(piles,h))