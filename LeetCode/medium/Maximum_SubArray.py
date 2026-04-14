# Problem: Maximum Subarray
# Find the contiguous subarray with the largest sum.
# Approach:
# first I tried a different approach which did made me to get close to my answer but some conditions were
# not meant 
# then I tried different approach all though both approaches takes the same time complexity and
# space complexity but this one met all the conditions 
# This approach utilizes Kadane algorithem
# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums):
        max_sub=nums[0]
        temp_sub=nums[0]
        for i in range(1,len(nums)):
            temp_sub=max(nums[i],temp_sub+nums[i])
            max_sub=max(max_sub,temp_sub)
        return max_sub