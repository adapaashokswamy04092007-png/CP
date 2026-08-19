class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max,current=0,0
        while True:
            if current+nums[current]>max:            
                max=current+nums[current]
            if max>=len(nums)-1:
                return True
            if current==max:
                break
            current+=1
        return False
            