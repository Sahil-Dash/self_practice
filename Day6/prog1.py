class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i=0
        while i<=len(nums)-1:
            if nums[i]=="_":
                break

            if i+2<=len(nums)-1 and nums[i]==nums[i+2]:
                nums.pop(i)
                nums.append("_")
                continue
            else:
                i+=1
        return i


sol=Solution()
arr=[0]
res=sol.removeDuplicates(arr)
print(res)