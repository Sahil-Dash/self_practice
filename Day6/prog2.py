class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n  # Handle cases where k is greater than n

        # Reverse the entire list
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])


        
        



nums = [1,2,3,4,5,6,7]
k = 3

Solution().rotate(nums,k)
print(nums)