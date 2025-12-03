class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in dict:
                return [dict[diff],i]
            dict[num]=i
        return []