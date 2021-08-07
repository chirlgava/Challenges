class Solution:
    def __init__(self):
        super().__init__()
    def numJewelsInStones(self, jewels, stones) :
        cont=0
        for jewel in jewels:
            for stone in stones:
                if jewel==stone:
                    cont+=1
            

        return cont



a=Solution()
print(a.numJewelsInStones('aA','aAAbbbb'))

print(a.numJewelsInStones('z','ZZ'))