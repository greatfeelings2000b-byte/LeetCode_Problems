# Problem: Group Anagrams
# Approach:
# In this problem we have to find the anagrams and list the same one in the same list we used a simple approach
# where we sorted the strings then join them having alphabetically sorted string and assigned it as key in the dictionary
# then we check if the key is already present in the dictionary and if not then we create a new key and assign empty list
# then we append the word in the list of the respective key after the loop ends we return the list of values of the dictionary
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
class Solution:
    def groupAnagrams(self, strs):
        dic = {}

        for word in strs:
            key = "".join(sorted(word)) 

            if key not in dic:
                dic[key] = []

            dic[key].append(word)

        return list(dic.values())