#problem Statement:Given an integer array nums, return an array answer such that answer[i] is equal to the product of
# all the elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    output=[1]*len(nums)
    # forward pass : for prefix
    prefix = 1
    for i in range(0,len(nums)):
        output[i] = prefix
        prefix*=nums[i]
    
    #backward pass : for suffix    
    postfix = 1
    for i in reversed(range(0,len(nums))):
        output[i]*= postfix
        postfix*=nums[i]
    return output
    
print(productExceptSelf([1,2,3,4]))