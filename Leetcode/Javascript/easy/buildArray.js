/**
 * 1920. Build Array from Permutation
 * https://leetcode.com/problems/build-array-from-permutation/

 */
 var buildArray = function(nums) {
    let saida=[]
    for(let i=0; i<nums.length; i++){
        saida.push(nums[nums[i]])
    }
    return saida
};

console.log(buildArray([0,2,1,5,3,4]))
console.log('expected: [0,1,2,4,5,3]')

console.log(buildArray([5,0,1,2,3,4]))
console.log('expected: [4,5,0,1,2,3]')
