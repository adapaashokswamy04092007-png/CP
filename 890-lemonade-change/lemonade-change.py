# 860. Lemonade Change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n=len(bills)
        change=[]
        for bill in bills:
            if bill==5:
                change.insert(0,5)
            elif bill==10:
                if change and change[0]==5:
                    change.pop(0)
                    change.append(10)
                else:
                    return False
            else:

                if len(change)>1 and change[0]==5 and change[-1]==10:
                    change.pop()
                    change.pop(0)
                elif len(change)>2:
                    for _ in range(3):
                        change.pop(0)
                else:
                    return False
        return True