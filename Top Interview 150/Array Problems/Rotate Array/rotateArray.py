#Problem Statement: Given an integer array nums, rotate the array to 
# the right by k steps, where k is non-negative.

#url: https://leetcode.com/problems/rotate-array/


from ast import List


def rotate( nums, k: int) -> None:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    size = len(nums)
    result =[0]*size
    
    for i in range(0,size):
        if i+k<size:
            result[i+k] = nums[i]
        else:
            s = (i+k)%size
            result[s] = nums[i]
    print(result)
    for i in range(0,size):
        nums[i]=result[i]
    


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    size = len(nums)
    k = k%size

    l,r = 0,size-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1

    l,r = 0, k-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1

    l,r = k,size-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1