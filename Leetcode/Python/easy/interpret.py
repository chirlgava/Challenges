
class Solution:
    def __init__(self):
        super().__init__()
    def interpret(self, command: str) -> str:
        '''
        '''
        command=command.replace('()','o')
        command=command.replace('(al)','al')
        return command

print(Solution().interpret("G()(al)"))
print(Solution().interpret("G()()()()(al)"))