var interpret = function(command) {
    var ans = command.split('()').join('o')
    ans=ans.split('(al)').join('al')
    return ans
};
console.log(interpret("G()(al)"))
console.log(interpret("G()()()()(al)"))
