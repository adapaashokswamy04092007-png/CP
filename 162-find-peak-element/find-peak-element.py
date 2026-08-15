class Solution:
    def _peak(self,arr,left,right):
        if left==right:
            return left
        mid=(left+right)//2
        
        if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
            return mid
                
        if arr[mid]<arr[mid+1]:
            return self._peak(arr,mid,right)
                    
        if arr[mid-1]>arr[mid]:
            return self._peak(arr,left,mid)    

    def findPeakElement(self, nums: List[int]) -> int:                    
        new_arr=[float("-inf")]+nums+[float("-inf")]
        return self._peak(new_arr,0,len(new_arr)-1)-1