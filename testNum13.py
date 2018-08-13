# 作者 ljc
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)
        """
        r_sum = 0
        rul = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for ch in s:
            ch_val = int(rul[ch])
            r_sum = r_sum + ch_val
        return r_sum




solution = Solution()
print(solution.romanToInt("MCMXCVI"))
