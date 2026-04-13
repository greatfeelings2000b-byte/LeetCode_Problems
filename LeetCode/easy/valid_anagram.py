# Valid Anagram
# First I tried the brute force method where I used loops and empty list to store char and used some conditions to return True or False
# but the brute force time complexity was O(n^2)
# So for optimal solution I used a dictionary (hashmap) to count character frequencies
# Count characters in t, then decrease counts using s and returning false if any of the condition did not met it reduce our time complexity
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1
        for char in s:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        return True