class Solution:
    def checkValidString(self, s: str) -> bool:
        min,max=0,0
        for ch in s:
            if ch=='(':
                min+=1
                max+=1
            elif ch==')':
                min-=1
                max-=1
            else:
                min-=1
                max+=1
            if max<0:
                return False
            if min <0 :
                min =0
        if min == 0:
            return True
        else :
            return False