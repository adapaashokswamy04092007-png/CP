class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps,min,max=0,0,0
        while max<len(nums)-1:
            farthest=max
            for i in range(min,max+1):
                if farthest<i+nums[i]:
                    farthest=i+nums[i]
            min=max+1
            max=farthest
            jumps+=1
        return jumps
