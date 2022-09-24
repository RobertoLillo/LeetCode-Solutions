class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                counter = 0
            maxLength = max(maxLength, counter)
        return maxLength