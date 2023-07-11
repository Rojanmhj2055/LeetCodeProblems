# Problem Statement: A phrase is a palindrome if, after converting all 
# uppercase letters into lowercase letters and removing all non-alphanumeric
# characters, it reads the same forward and backward. Alphanumeric character
# s include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

import re
def isPalindrome(self, s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = s.lower()


    return s ==s[::-1]
