class Solution:
    def __init__(self):
        super().__init__()

    
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for circle in queries:
            cont=0
            for point in points:
                if (point[0]-circle[0])**2+(point[1]-circle[1])**2<=circle[2]**2:
                    cont +=1
            ans.append(cont)
        return ans

#(x - a)2 + (y - b)2 =r2
a=Solution()
print(a.countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))

print(a.countPoints([[1,1],[2,2],[3,3],[4,4],[5,5]],[[1,2,2],[2,2,2],[4,3,2],[4,3,3]]))