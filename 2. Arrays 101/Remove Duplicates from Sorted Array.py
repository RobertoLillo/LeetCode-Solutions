class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != nums[pointer]:   
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1