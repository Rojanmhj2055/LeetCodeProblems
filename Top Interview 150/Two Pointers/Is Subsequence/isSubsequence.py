# Problem Statement:Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#                   A subsequence of a string is a new string that is formed from the original string by
#                   deleting some (can be none) of the characters without disturbing the relative positions
#                   of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Input: s = "axc", t = "ahbgdc"
# Output: false

def isSubsequence(self, s: str, t: str) -> bool:
    i = 0  # pointer for s
    j = 0  # pointer for t
    while i < len(s) and j < len(t):
        if s[i] == t[j]:  
            i += 1
        j += 1  
    return i == len(s)