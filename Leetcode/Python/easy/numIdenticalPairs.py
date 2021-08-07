class Solution:
    def __init__(self):
        super().__init__()
    
    def numIdenticalPairs(self, nums) :
        """
        :type nums: List[int]
        """
        cont=0
        for num1 in nums:
            for num2 in nums:
                if num1==num2:
                    cont+=1

        return int((cont-len(nums))/2)


a=Solution()
print(a.numIdenticalPairs([1,2,3,1,1,3]))
print(a.numIdenticalPairs([1,1,1,1]))
print(a.numIdenticalPairs([1,2,3]))
