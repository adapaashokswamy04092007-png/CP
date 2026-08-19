class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        max = float('-inf')
        count=0
        c_co,r_co,o_co,a_co,k_co=0,0,0,0,0
        if croakOfFrogs[0]!='c':
            return -1
        for i in croakOfFrogs :
            if i=='c':
                count+=1
                c_co+=1
            elif i=='r':
                r_co+=1
            elif i=='o':
                o_co+=1
            elif i=='a':
                a_co+=1
            elif i=='k':
                count-=1
                k_co+=1
            if count>max:
                max=count
            if c_co>=r_co:
                if r_co>=o_co:
                    if o_co>=a_co:
                        if a_co>=k_co:
                            continue
            return -1
            
        if c_co==r_co:
            if r_co==o_co:
                if o_co==a_co:
                    if a_co==k_co:
                        return max
        return -1