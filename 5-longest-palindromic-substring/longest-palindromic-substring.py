class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        self.start = 0
        self.max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > self.max_len:
                    self.start = left
                    self.max_len = right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)       # Odd length
            expand(i, i + 1)   # Even length

        return s[self.start:self.start + self.max_len]