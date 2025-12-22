"""
394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                curr_str = ""
                while stack and stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                stack.pop()
                number_str = ""
                while stack and stack[-1].isdigit():
                    number_str = stack.pop() + number_str
                stack.append(int(number_str) * curr_str)
        return "".join(stack)

sol = Solution()
s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
print(sol.decodeString(s))