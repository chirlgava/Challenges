#1470. Shuffle the Array
#https://leetcode.com/problems/shuffle-the-array/
def shuffle(nums, n):
    ans=[]
    for i in range(0,int(n)):
        ans.append(nums[i])
        ans.append(nums[i+int(n)])
    return ans




print(shuffle([1,2,3,4,4,3,2,1],4))
print('output: [1,4,2,3,3,2,4,1]')
