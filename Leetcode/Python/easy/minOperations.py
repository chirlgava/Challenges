class Solution:
    def __init__(self):
        super().__init__()
    def minOperations(self,boxes):
        """
        boxes:string
        """
        lista=[]
        pos=[]
        cont=0
        for number in boxes:
            lista.append(int(number))
            if int(number)==1:
                pos.append(cont)
            cont+=1
        for i in range(0,len(lista)):
            res=0
            for num in pos:
                res=res+abs(i-num)
            lista[i]=res

        return lista


a=Solution()
print(a.minOperations("001011"))
print(Solution().minOperations("001011"))