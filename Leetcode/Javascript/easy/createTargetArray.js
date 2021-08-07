var createTargetArray = function(nums, index) {
    new_list=[]
    for(const indice in index){
      new_list.splice(index[indice],0,nums[indice])
    }
    
    return new_list
      
  }
  console.log(createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
  console.log([0,4,1,3,2])