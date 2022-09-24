class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3 or arr[0] > arr[1]:
            return False
        top = False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            elif not top and arr[i] > arr[i + 1]:
                top = True
            elif top and arr[i] < arr[i + 1]:
                return False
        return True if top else False