# 作者 ljc
# 给出一个整数，写一个函数来确定这个数是不是3的一个幂。
#
# 后续挑战：
# 你能不使用循环或者递归完成本题吗？
class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0