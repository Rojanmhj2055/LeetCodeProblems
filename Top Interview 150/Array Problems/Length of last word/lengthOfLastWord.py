#Problem Statement: Given a string s consisting of words and spaces, return the length of the last word in the string 
# A word is a maximal substring consisting of non-space characters only.

#url:https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord( s: str) -> int:
    st = s.split(" ")
    if len(st)>0:
        for i in reversed(range(0,len(st))):
            if len(st[i])>0:
                return len(st[i])
    else:
        return 1
    

## better solution
def lengthOfLastWord(s:str)->int:
    st = s.strip()
    st = st.split(" ")
    return len(s[-1])
