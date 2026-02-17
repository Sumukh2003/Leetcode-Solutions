class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res=[]
        for hour in range(12):
            for min in range(60):
                if(bin(hour).count('1')+bin(min).count('1') == turnedOn):
                    res.append("{}:{:02d}".format(hour,min))
        return res