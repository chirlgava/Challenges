#1920. Build Array from Permutation
#https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def __init__(self):
        super().__init__()
    def buildArray(self, nums):
        """
        nums: List[int]
        return:List[int]
        """
        saida=[]
        for num in nums:
            saida.append(nums[num])
        return saida

print(Solution().buildArray([0,2,1,5,3,4]))
print('expected: [0,1,2,4,5,3]')
print(Solution().buildArray([5,0,1,2,3,4]))
print('expected: [4,5,0,1,2,3]')