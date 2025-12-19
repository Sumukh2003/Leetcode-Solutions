class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split()
        word=s[-1]
        count=0
        for i in range(len(word)):
            count+=1
        return count