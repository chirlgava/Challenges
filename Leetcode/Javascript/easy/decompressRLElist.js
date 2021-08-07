var decompressRLElist = function(nums) {
    resposta=[]
    for (i = 0; i < nums.length; i=i+2) {
        for (cont=0;cont<nums[i];cont++) {
            resposta.push(nums[i+1])
        }
      } 
    return resposta
}
console.log(decompressRLElist([1,2,3,4])) 