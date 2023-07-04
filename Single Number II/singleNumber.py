#Problem Statement: Given an integer array nums where every element appears three times except for one, 
# which appears exactly once. Find the single element and return it. You must implement a solution with 
# a linear runtime complexity and use only constant extra space

# url: https://leetcode.com/problems/single-number-ii/

def singleNumber(nums)->int:
    count={}
    for i in nums:
        if i in count:
            count[i]= count[i]+1
        else:
            count[i] = 1
    for key, value in count.items():
        if value == 1:
            return key
    return 0
