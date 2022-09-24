class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 101
                counter -= 1
        nums.sort()
        return counter