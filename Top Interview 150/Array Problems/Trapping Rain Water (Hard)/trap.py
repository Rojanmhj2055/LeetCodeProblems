#Problem Description: Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
#Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array 
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Hard Problem 

height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = 6

## Time Complexity = O(n), Space Complexity= O(n)
def trap(height)->int:
    
    maxLeft=[0]*len(height)
    maxRight=[0]*len(height)
    
    #Calculate the maximum height to the left 
    maxTillNow= 0
    for i in range(len(maxLeft)):
        maxLeft[i] = maxTillNow
        maxTillNow = max(maxTillNow,height[i])
    
    #Calculate the maximum height from the right 
    maxTillNow = 0
    for i in reversed(range(0,len(height))):
        maxRight[i] = maxTillNow
        maxTillNow = max(maxTillNow,height[i])
        
    #calculate minmum between maxLeft and maxRight at index i
    totalWater = 0
    for i in range(len(height)):
        diff = min(maxLeft[i],maxRight[i]) - height[i]
        if diff>0:
            totalWater+=diff
    return totalWater

## Two pointer solution
## Time Complexity: O(n) and Space Complexity: O(1)
def trap(height)->int:
    totalWater = 0
    if not height: return 0
    l,r =0,len(height)-1
    
    leftMax, rightMax = height[l],height[r]
    
    while l<r:
        if leftMax<rightMax:
            l+=1
            leftMax = max(leftMax,height[l])
            totalWater+=leftMax-height[l]
        else:
            r-=1 
            rightMax = max(rightMax,height[r])
            totalWater+= rightMax-height[r]
    
    return totalWater