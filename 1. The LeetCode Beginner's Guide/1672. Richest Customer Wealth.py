class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_value = 0
        for i in accounts:
            if sum(i) > max_value:
                max_value = sum(i)
        return max_value