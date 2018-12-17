
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
#时间复杂度 O（n²）
class Solution():
    def twoSum(nums, target):
        nums=list(nums)
        target=int(target)
        s=len(nums)
        for i in range(s):
            for j in range(i+1,s):
                if nums[i]+nums[j]==target:
                    #return[i,j] return 最终只返回一组，但是print可以返回所有可能情况
                    print(i,j)
                else:
                    continue
——————————————————————————————————————————————————————————————
Solution.twoSum([1,2,3,7,4],5)

#关于self
class Solution():
    def __init__(self,nums,target):
        self.nums=list(nums)
        self.target=int(target)
    def Twosum(nums,target):
        s=len(nums)
        for i in range(s):
            for j in range(i+1,s):
                if nums[i]+nums[j]==target:
                    print(i,j)
                else:
                    continue
   _________________________________________________                 
  Solution.Twosum([1,2,3,7,4,4],5)
  #需改进，并没有判别是否为nums是否为list,target是否为int
