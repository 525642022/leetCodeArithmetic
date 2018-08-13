# 作者 ljc
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 案例：
# a = "11"
# b = "1"
# 返回 "100" 。\
# 思路二进制转换为十进制，相加求和，在把结果转换为二进制
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


solution = Solution()
solution.addBinary('101', '110')
