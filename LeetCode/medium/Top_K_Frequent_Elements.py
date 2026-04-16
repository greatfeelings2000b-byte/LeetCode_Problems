# Problem: Top K Frequent Elements

# Approach:
# Count frequency using a dictionary
# Repeatedly find the element with maximum frequency
# Remove it from dictionary after selecting
# Repeat k times to get top k elements

# It uses repeated max search.
# The time complexity depends upon the number of run using k so that is why time complexity is 
# Time Complexity: O(n * k)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums, k):
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        result = []

        for _ in range(k):
            max_key = max(dic, key=dic.get)
            result.append(max_key)
            del dic[max_key]

        return result