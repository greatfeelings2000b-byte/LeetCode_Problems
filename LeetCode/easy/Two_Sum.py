# Problem: Two Sum
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to the target.

# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

# Approach: Brute Force
# - Iterate through all possible pairs
# - Check if their sum equals the target
# - Return the indices when found

# Time Complexity: O(n^2)

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]