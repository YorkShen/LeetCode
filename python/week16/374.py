# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        def guessNumber(lo, hi):
            mid = (lo + hi) / 2
            ret = guess(mid)
            if ret == 0:
                return mid
            elif ret == -1:
                return guessNumber(lo, mid - 1)
            elif ret == 1:
                return guessNumber(mid + 1, hi)

        return guessNumber(0, n)
