class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        """
        items: List[List[str]], 
        ruleKey: str, 
        ruleValue: str 
        return: int
        """
        def first():
            cont=0
            for item in items:
                if item[0]==ruleValue:
                    cont+=1
            return cont
        def second():
            cont=0
            for item in items:
                if item[1]==ruleValue:
                    cont+=1
            return cont
        def third():
            cont=0
            for item in items:
                if item[2]==ruleValue:
                    cont+=1
            return cont
        
        options={"type":first,
        "color":second,
        "name":third,}
        return options[ruleKey]()

print(Solution().countMatches( [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver"))