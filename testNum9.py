class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return `x`[::-1] == `x`
        if x < 0:
            return False
        resNum = 0
        print()
        while (x > resNum):
            resNum = resNum * 10 + x % 10
            x = x / 10
        print(x, resNum)
        return x == resNum | x == int(resNum) / 10


solution = Solution()
print(solution.isPalindrome(1))
