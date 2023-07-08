#Problem description: Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

def minSubArrayLen(self, target: int, nums) -> int:
    left = 0
    sum = 0
    res = len(nums)+1 # or Math.Infinity
    for r in range(len(nums)):
        sum+=nums[r]
        while sum>=target:
            sum-=nums[left]
            res = min(r-left+1,res)
            left+=1
    return 0 if res==len(nums)+1 else res