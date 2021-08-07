class Solution:
    def __init__(self):
        super().__init__()
    def smallerNumbersThanCurrent(self, nums) :
        """
        nums:list[int]
        """
        lista=[]
        for num in nums:
            cont=0
            for num2 in nums:
                if num>num2:
                    cont+=1
            lista.append(cont)
        return lista

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
