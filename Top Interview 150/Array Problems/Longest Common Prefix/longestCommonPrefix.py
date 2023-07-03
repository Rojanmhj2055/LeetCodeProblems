#Problem Statement:Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

#url: https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs)->str:
    if len(strs)== 0 or strs == None:
        return ""
    prefix = strs[0]
    
    for i in range(1,len(strs)):
        j = 0 
        current = strs[i]
        while j < len(current) and j < len(prefix) and prefix[j] == current[j]:
            j+=1
        
        if j == 0:
            return ""
        
        prefix = current[0:j]
    
    return prefix