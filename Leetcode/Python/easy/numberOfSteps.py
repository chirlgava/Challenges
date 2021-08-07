
class Solution:
    def __init__(self):
        super().__init__()
    def numberOfSteps(self, num):
        """
        num:int
        """
        cont=0
        while num != 0:
            if num%2==0:
                num=num/2
                cont+=1
            else:
                num=num-1
                cont+=1
        return cont

print(Solution().numberOfSteps(14))
print(Solution().numberOfSteps(123))
