class Solution(object):
    def twoSum(self,nums,target):
        d={}
        for i,num in enumerate(nums):
            
            b=target-num
            if b in d:
                return[d[b],i]
           
            d[num]=i


        