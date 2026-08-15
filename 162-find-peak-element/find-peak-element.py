class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        def peak(arr,left,right):
            if left==right:
                return left
            mid=(left+right)//2
            
            if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
                return mid
                
            if arr[mid]<arr[mid+1]:
                return peak(arr,mid,right)
                    
            if arr[mid-1]>arr[mid]:
                return peak(arr,left,mid)
                    
        new_arr=[float("-inf")]+nums+[float("-inf")]
        return peak(new_arr,0,len(new_arr)-1)-1