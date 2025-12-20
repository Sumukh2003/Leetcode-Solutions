class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        delete=0
        rows=len(strs)
        cols=len(strs[0])
        for col in range(cols):
            for row in range(1,rows):
                if strs[row][col] < strs[row-1][col]:
                    delete+=1
                    break
        return delete
