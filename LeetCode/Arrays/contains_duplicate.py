# I first tried the brute force technique similar to the one Two_Sums
# Then I trade of time complexity with space complexity by using set and removing extra loop
# set stores only distinct value which helps us to locate any duplicate if present 
# If an element is already in the set → duplicate found
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False