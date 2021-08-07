#1431. Kids With the Greatest Number of Candies
#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(candies, extraCandies):
    sol=[]
    for i in candies:
        if i+extraCandies>=max(candies):
            sol.append(True)
        else:
            sol.append(False)
    return sol

print(kidsWithCandies([2,3,5,1,3],3))
print("Output: [true,true,true,false,true] ")





def defangIPaddr(address):
    return address.replace('.','[.]')


print(defangIPaddr("1.1.1.1"))