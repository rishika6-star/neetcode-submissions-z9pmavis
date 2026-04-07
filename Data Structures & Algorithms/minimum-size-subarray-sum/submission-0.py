class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        Min = float('inf')
        h = 0  
        l = 0
        s = 0
        for i in  nums:
            s = s + i
        if(s < target):
            return 0
        while(h < n):
            sum = sum + nums[h]
            while(sum >= target):
                length = h - l + 1
                Min = min(Min , length) 
                sum = sum - nums[l]
                l += 1
            h += 1
       
        return Min       

        