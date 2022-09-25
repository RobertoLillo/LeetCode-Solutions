class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1: len(arr)])
        arr[-1] = -1
        return arr