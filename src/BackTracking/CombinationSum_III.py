"""
216. Combination Sum III
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(sum_remaining, comb, next_start):
            if sum_remaining == 0 and len(comb) == k:
                result.append(list(comb))
                return
            elif sum_remaining < 0 or len(comb) == k:
                return
            remaining_count = k - len(comb)
            if remaining_count > 0:
                min_sum = remaining_count * next_start + (remaining_count * (remaining_count - 1))/2
                if min_sum > sum_remaining:
                    return
            for i in range(next_start, min(10, sum_remaining + 1)):
                comb.append(i)
                backtrack(sum_remaining - i, comb, i + 1)
                comb.pop()
        backtrack(n, [], 1)
        return result

sol = Solution()
k = 3
n = 7
k = 3
n = 9
k = 4
n = 1
print(sol.combinationSum3(k,n))