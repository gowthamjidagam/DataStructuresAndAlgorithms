"""
334. Increasing Triplet Subsequence
Medium
Topics
premium lock icon
Companies
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        first = float("inf")
        second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

    def increasingTriplet2(self, nums):
        """
        This will return actual indices
        :param nums:
        :return:
        """
        n = len(nums)
        smallest = float("inf")
        smallest_idx = -1
        sec_smallest = float("inf")
        sec_smallest_idx = -1
        sec_small_idx = -1
        for i in range(n):
            if nums[i] <= smallest:
                smallest = nums[i]
                smallest_idx = i
            elif nums[i] <= sec_smallest:
                sec_smallest = nums[i]
                sec_smallest_idx = i
                sec_small_idx = smallest_idx
            else:
                return (sec_small_idx,sec_smallest_idx,i)

nums = [2,1,5,0,4,6]
nums = [5,4,3,2,1]
nums = [1,2,3,4,5]
nums = [10,20,3,2,1,1,2,0,4]
sol = Solution()
print(sol.increasingTriplet(nums))
print(sol.increasingTriplet2(nums))