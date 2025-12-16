"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return nums[::-1]
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = []
        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i+1]
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res

    def productExceptSelf2(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return nums[::-1]

        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

sol = Solution()
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))
print(sol.productExceptSelf2(nums))