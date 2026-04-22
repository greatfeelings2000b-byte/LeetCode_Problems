# Problem: Move Zeroes
# Approach:
# In this problem we make two pointers named right and left. Right is used for iteration and Left one is for looking zero if zero
# is found then the condition gets skip and now previous iteration have left pointer and next one non zero has right pointer 
# now swapping happens and if we get into another zero then again the condition gets skip and the left pointer now stays 2 step
# behind the the right pointer and swaps happens skipping middle zero in between it keeps going till the loop ends and we gets 
# the modified array with all the zeros at the end irrespective of how many zeros were there.
# Time Complexity O(n)
# Space COmplexity O(1)

class Solution:
    def moveZeroes(self, nums):
       left=0
       for right in range(len(nums)):
          if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
       return nums

