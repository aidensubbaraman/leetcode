class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        xString = str(x)

        xLength = len(xString)

        for i in range(xLength // 2): # Use '//' for integer division

            if xString[i] != xString[xLength - i - 1]:
                return False

        return True