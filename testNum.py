# 作者 ljc
nums = [2, 3, 1, 4]
target = 6
setNums = {}
for index, item in enumerate(nums):
    m = target - item
    if m in setNums:
        print(setNums[m],index)
    else:
        setNums[item] = index

nums = [2,3,1,4]
target = 6
sunNums = {}
for index , item  in enumerate(nums):
    m = target = item
    if m in  setNums:
        print(setNums[m],index)


