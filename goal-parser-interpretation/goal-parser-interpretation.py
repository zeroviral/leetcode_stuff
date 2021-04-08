class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        vals = []
        
        for i in range(len(command)):
            if 0 <= i < len(command) - 1 and command[i] == "(":
                if command[i + 1] == ")":
                    vals.append("o")
            elif command[i] != ")":
                vals.append(command[i])
        return "".join(vals)
        