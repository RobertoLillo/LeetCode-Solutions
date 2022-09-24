class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for number in nums:
            result.append(number**2)
        return (sorted(result))