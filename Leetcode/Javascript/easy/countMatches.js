var countMatches = function(items, ruleKey, ruleValue) {
    switch(ruleKey) {
      case "type":
      var ans=0  
      for(const i in items){
          if (items[i][0]==ruleValue){
            ans=ans+1
            }
        }
        break;
      case "color":
        var ans=0  
        for(const i in items){
            if (items[i][1]==ruleValue){
              ans=ans+1
              }
          }
  
        // code block
        break;
      case "name":
        var ans=0  
        for(const i in items){
            if (items[i][2]==ruleValue){
              ans=ans+1
              }
          }
  
      default:
        // code block
    }   
    return ans
  };
  
  console.log(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver"))