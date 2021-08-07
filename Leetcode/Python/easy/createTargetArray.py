class Solution:
    def __init__(self):
        super().__init__()
    def createTargetArray(self, nums, index):
        """
        nums:List[int]
        index:List[int]
        return :List[int]
        """
        new_list=[]
        # text=''
        cont=0
        for indice in index:
            new_list.insert(indice,nums[cont])
            cont+=1


        return new_list

print(Solution().createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
print([0,4,1,3,2])