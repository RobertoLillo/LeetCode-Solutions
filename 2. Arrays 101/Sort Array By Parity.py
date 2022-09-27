class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[pointer] % 2 != 0:
                nums.append(nums[pointer])
                del nums[pointer]
            else:
                pointer += 1
        return nums