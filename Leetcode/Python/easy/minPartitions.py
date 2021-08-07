class Solution:
    def __init__(self):
        super().__init__()
    def minPartitions(self, n):
        """
        n: string
        """
        lista=[]
        for number in n:
            lista.append(int(number))
        return max(lista)


a=Solution()
print(a.minPartitions("82734"))
print(a.minPartitions("27346209830709182346"))