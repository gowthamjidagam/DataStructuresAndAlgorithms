"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = 0
        j = 0
        while j < k:
            if s[j] in "aeiou":
                vowels += 1
            j += 1
        max_vowels = vowels
        for x in range(j, len(s)):
            if s[x] in "aeiou" and s[x-k] not in "aeiou":
                vowels += 1
            elif s[x] not in "aeiou" and s[x-k] in "aeiou":
                vowels -= 1
            max_vowels = max(max_vowels, vowels)
        return max_vowels

    def maxVowels2(self, s, k):
        vowels = set("aeiou")
        count = sum(c in vowels for c in s[:k])
        max_vowels = count
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i-k] in vowels)
            max_vowels = max(max_vowels, count)
        return max_vowels

s = "abciiidef"
k = 3
s = "aeiou"
k = 2
s = "leetcode"
k = 3
s = "weallloveyou"
k = 7
sol = Solution()
print(sol.maxVowels(s,k))
print(sol.maxVowels2(s,k))