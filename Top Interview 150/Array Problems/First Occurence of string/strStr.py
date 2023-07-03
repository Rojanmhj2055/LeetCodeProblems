#problem statement:Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#url: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


def strStr(haystack:str,needle:str)->int:
    ptr =0
    while ptr< len(haystack) and ptr+len(needle)<=len(haystack):
        s = haystack[ptr:ptr+len(needle)]
        print(s)
        if s == needle:
            return ptr
        ptr = ptr+1
    
    
    return -1
    
## another solution 
# def strStr(haystack:str,needle:str) ->int:
#     for i in range(len(haystack)):
#         if haystack[i:].startswith(needle):
#             return i
#     return -1

## another solution
