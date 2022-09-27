class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        counter = 0
        sortedHeights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                counter += 1
        return counter