class Solution:
    def interpret(self, command: str) -> str:
        ret = ""
        # pretty self explanatory, cut off the alphabet while still stuff in command
        while len(command) > 0:
            if command[0] == 'G':
                ret += 'G'
                command = command[1:]
            elif command[:2] == '()':
                ret += 'o'
                command = command[2:]
            else:
                ret += 'al'
                command = command[4:]
        return ret
