"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        hashmap = defaultdict(int)
        count = 0
        for n in nums:
            complement = k - n
            if complement in hashmap and hashmap[complement] > 0:
                count += 1
                hashmap[complement] -= 1
            else:
                hashmap[n] += 1
        return count

    def maxOperations2(self, nums, k):
        """
        using two pointers
        :param nums:
        :param k:
        :return:
        """
        nums = sorted(nums)
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1
        return count

sol = Solution()
nums = [1,2,3,4]
k = 5
# nums = [3,1,3,4,3]
# k = 6
print(sol.maxOperations(nums,k))
print(sol.maxOperations2(nums,k))