class Solution:
    def __init__(self):
        super().__init__()
    def subtractProductAndSum(self, n):
        """
        n:int
        """
        prod=1
        soma=0
        text=str(n)
        for letter in text:
            prod=prod*int(letter)
            soma=soma+int(letter)
        return prod-soma
