class Solution(object):
    def removeElement(self, nums, val):
        n=0
        for i in range(0,len(nums)):
            if nums[i] !=val:
                nums[i],nums[n]=nums[n],nums[i]
                n +=1
        return n