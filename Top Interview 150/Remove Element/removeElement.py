#Problem statement: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#url:https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

def removeElement(nums,val:int) ->int:
       k = 0

       for i in range(len(nums)):
           if nums[i]!=val:
               nums[k] = nums[i]
               k = k+1
        
       return k