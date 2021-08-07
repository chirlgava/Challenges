def runningSum(nums):
    
    total=len(nums)
    i=0
    solution=[]
    while i<total:
        cont=0
        temp=nums[i]
        for b in nums:
            if cont == i:
                solution.append(temp)
                break
            temp=temp+b
            cont=cont+1
        i=i+1
    
    return solution


print(runningSum([1,2,3,4]))
print('expected value:[1,3,6,10]')
print(runningSum([1,1,1,1,1]))
print('expected value:[1,2,3,4,5]')
print(runningSum([3,1,2,10,1]))
print('expected value:[3,4,6,16,17]')
