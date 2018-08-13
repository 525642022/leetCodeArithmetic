# 作者 ljc
# 编写一个函数，输入是一个无符号整数，返回的是它所有 位1 的个数（也被称为汉明重量）。
#
# 例如，32位整数 '11' 的二进制表示为 00000000000000000000000000001011，所以函数返回3。
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return len(i for i in range(32) if(1<<i)&n)