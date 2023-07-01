#Problem Statement: Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

#url:https://leetcode.com/problems/majority-element/

from ast import List


def majorityElement(self, nums: List[int]) -> int:
    count = 0
    answer =0
    
    for i in nums:
        if count ==0:
            answer = i
        if i == answer:
            count = count+1
        else:
            count = count-1
    
    return answer