class Solution(object):
    def jump(self,nums):
        n = len(nums)
        if n <= 1:
            return 0

        jump = 0
        curr_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            print(farthest, i, nums[i])
            if i == curr_end:
                jump += 1
                curr_end = farthest

        return jump


        

arr=[2,3,1,1,4]

res=Solution().jump(arr)
print(res)