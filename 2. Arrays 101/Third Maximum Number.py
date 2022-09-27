class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = []
        for i in nums:
            if i not in distinct:
                distinct.append(i)
            distinct.sort()
            distinct = distinct[::-1]
        if len(distinct) >= 3:
            return (distinct[2])
        else:
            return (distinct[0])