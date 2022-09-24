class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for number in nums:
            counter = 1
            while number // 10 != 0:
                number = number // 10
                counter += 1
            if counter % 2 == 0:
                result += 1
        return result