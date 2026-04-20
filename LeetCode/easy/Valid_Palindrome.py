# Problem: Valid Palindrome
# Approach:
# In this problem we have to create a new string m and then we have to iterate through the given string and check if the character
# is alphanumeric or not if it is then we have to convert it to lowercase and add it to the new string m then we have to check 
# if the new created string m is equal to its reverse or not if it is then we return true else we return false
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ""
        for c in s:
            if c.isalnum():       
                m += c.lower()
        
        return m == m[::-1]      