#problem Statement: Jump Game I
#You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#Return true if you can reach the last index, or false otherwise.


def jumpGame(nums) -> bool:
    farthest, last_index = 0, len(nums)-1
    
    i = 0
    
    while i<=farthest and farthest<last_index:
        farthest = max(farthest,i+nums[i])
        i = i+1
        
    return farthest >=last_index
    
    
    
# problem statement: Jump Game II
#You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at
# nums[i], you can jump to any nums[i + j] where:0 <= j <= nums[i] and #i + j < n
#Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
    
def jump(self, nums) -> int:
    res = 0
    l=r=0

    while r<len(nums)-1:
        farthest = 0
        for i in range(l,r+1):
            farthest = max(farthest,i+nums[i])

        l=r+1
        r=farthest
        res+=1
    
    return res