#https://leetcode.com/problems/richest-customer-wealth/
#1672. Richest Customer Wealth
class Solution():
    def __init__(self,accounts):
        self.accounts=accounts


    def maximumWealth(self):
        y=0
        for account in self.accounts:
            if sum(account)>y:
                y=sum(account)
        return y

a=Solution([[1,2,3],[3,2,1]])


def maximumWealth(accounts):
    y=0
    for account in accounts:
        if sum(account)>y:
            y=sum(account)
    return y

print(maximumWealth([[1,2,3],[3,2,1]]))