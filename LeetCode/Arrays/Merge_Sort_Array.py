
# Problem: 
# Merge Sorted Array

# ____ Approach 1 ____(Brute Force):
# Manually removed zeroes.
# merged two arrays
# Used bubble sort to solve the problem skipped due to greater time complexity

# ____ Approach 2 ____(Optimal):
# Use three pointers starting from the end of arrays.
# Compare elements and place the larger one at the end of nums1.
# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def merge(self, nums1, nums2, m, n):
        p1=m-1
        p2=n-1
        k=m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[k]=nums1[p1]
                p1-=1
            else:
                nums1[k]=nums2[p2]
                p2-=1
            k-=1
        while p2 >= 0:
            nums1[k] = nums2[p2]
            p2 -= 1
            k -= 1
       
       