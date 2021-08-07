def twoSum(nums,target):
    temp=nums
    length=len(nums)
    for num1 in nums:
        pos1=nums.index(num1)
        temp=[x+num1 for x in nums]
        temp[pos1]=target+1
        for resp in temp:
            if resp==target :
                pos2=temp.index(resp,pos1+1)
                return [pos1,pos2]



print(twoSum([2,7,11,15],9))
print('expected:',[0,1])

print(twoSum([2,5,5,11],10))

print('expected:',[1,2])



print(twoSum([3,2,4],6))
print('expected:',[1,2])
