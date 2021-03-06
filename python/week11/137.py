class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for num in nums:
            a, b = (a & ~b & ~num) | (~a & b & num), (~a & b & ~num) | (~a & ~b & num)
        return a | b
