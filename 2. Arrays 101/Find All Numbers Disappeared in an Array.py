class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        expectedArray = list(range(1,len(nums)+1)) 
        result = list(set(expectedArray) - set(nums))
        return result