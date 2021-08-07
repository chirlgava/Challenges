class Solution:
    def __init__(self):
        super().__init__()
    def decode(self, encoded, first):
        """
        encoded: list[int]
        first: int
        Return: List[int]
        """
        decoded=[first]
        cont=0
        for num in encoded:
            decoded.append(abs(decoded[cont]-num))
            cont=cont+1
        return decoded


print(Solution().decode([1,2,3],1))
print(Solution().decode([6,2,7,3],4))
