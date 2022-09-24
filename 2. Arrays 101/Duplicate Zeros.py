class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        position = 0
        while position < len(arr) - 1:
            if arr[position] == 0:
                arr.insert(position + 1, 0)
                arr.pop()
                position += 1
            position += 1