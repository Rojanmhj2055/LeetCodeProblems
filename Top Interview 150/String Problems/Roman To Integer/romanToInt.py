# Problem Statement: Given a Roman string return its Integer value

# url : https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150

def romanToInt(s:str)->int:
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    value = roman[s[-1]]
    for i in reversed(range(len(s)-1)):
        if roman[s[i]]<roman[s[i+1]]:
            value = value - roman[s[i]]
        else:
            value = value + roman[s[i]] 
    
    return value

## solution using Functool

import functools

def romanToInt(self, s: str) -> int:
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    return functools.reduce(
    lambda val,i: val+ (-roman[s[i]] if roman[s[i]] < roman [s[i+1]] else roman[s[i]]),reversed(range(len(s)-1)),roman[s[-1]])
    