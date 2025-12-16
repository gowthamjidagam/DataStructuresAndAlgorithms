#151. Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = []
        for w in range(len(words) - 1,-1,-1):
            res.append(words[w])
        return " ".join(res)

    def reverseWords2(self, s):
        if not s:
            return s
        return " ".join(s.split()[::-1])

sol = Solution()
s = "  hello world  "
s = "a good   example"
print(sol.reverseWords(s))
print(sol.reverseWords2(s))