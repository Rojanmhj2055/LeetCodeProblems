#Problem Statement:Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number 
# of unique elements in nums.

# url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from ast import List


def removeDuplicates(self, nums: List[int]) -> int:
    left = 1
    right = 1

    while right < len(nums):
        if nums[right-1]== nums[right]:
            right = right + 1
        else:
            nums[left] = nums[right]
            left = left + 1
            right= right+1
    
    return left