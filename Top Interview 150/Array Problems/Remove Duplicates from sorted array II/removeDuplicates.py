# Problem Statement:Given an integer array nums sorted in non-decreasing order, remove some 
# duplicates in-place such that each unique element appears at most twice. The relative order
# of the elements should be kept the same.

# url :https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from ast import List


def removeDuplicates(self, nums: List[int]) -> int:
    left = 1
    right = 1
    count = 1
    while right < len(nums):
        if nums[right-1] == nums[right] and count<=1:
            nums[left]=nums[right]
            right = right + 1
            count = count+1
            left = left + 1
        elif nums[right-1] == nums[right] and count>=2:
            right= right+1
            count = count+1
        else:
            nums[left] = nums[right]
            left = left+1
            right = right+1
            count=1 
    
    return left
