# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].


from ast import List
import math
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    index = 0
    result =[]
    prev_diff = -1001
    for i in range(len(numbers)):
        
        diff = target - numbers[i]
        if prev_diff == diff:
            continue
        prev_diff = diff
        j=i+1
        while j<len(numbers):
            if numbers[j] == diff:
                result.append(i+1)
                result.append(j+1)
                return result
            if numbers[j]>diff:
                break
            j=j+1
    
    return result