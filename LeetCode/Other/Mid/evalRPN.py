class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {'+', '-' , '*' , '/'} 
        res = []

        for token in tokens:
            if token in operators:
                op2 = res.pop()
                op1 = res.pop()
                if token == '+':
                    res.append(op1 + op2)
                elif token == '-':
                    res.append(op1 - op2)
                elif token == '*':
                    res.append(op1 * op2)
                else :
                    int(res.append(op1 / op2))
            else:
                res.append(int(token))
        return round(res.pop())

