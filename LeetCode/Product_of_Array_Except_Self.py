# Problem: Product of Array Except Self
# Approach:
# In this problem we used prefix and postfix pattern we could used two arrays i.e different approach
# with the same pattern by making two seperate arrays for both prefix and postfic then taking the product
# of both but it would have increases our space complexity and also time complexity so instead we just
# stored their product in the output and computing them within for loop.
# the math behind it looks like this: 
# result[i] = (product of left elements) * (product of right elements)
# where we compute the prefix and store them in output array res then we compute the postfix and multiply it 
# with the output array and also initializing the both prefix and postfix so that the product of all the array 
# except the one in position occurs.
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)

class Solution:
    def productExceptSelf(self, nums):
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]*=prefix
            prefix*=nums[i] 
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res