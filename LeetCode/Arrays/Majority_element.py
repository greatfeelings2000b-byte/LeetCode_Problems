# ----Problem:----

# Majority Element

# ----Approach:----

# __Brute Force:__
# In this method where we used dictionary to get the frequency of each elements.
# Then making condition frequency > n//2 to return the value.
# Time Complexity O(n)
# Space Complexity O(n)

# __Optimal Solution:__
# This method is called Boyer-Moore Voting Algorithm.
# Cancel out different elements; majority element remains.
# Time Complexity O(n)
# Space Complexity O(1)

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate