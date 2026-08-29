import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #Stack to keep track of the result
        st = []
        while tokens :
            print(f"The stack is {st}")
            item = tokens.pop(0)
            if item not in {'+', '-','*','/'}:
                st.append(int(item))
            else:
                match item:
                    case '+':
                        second_operand = st.pop()
                        first_operand = st.pop()
                        st.append(first_operand + second_operand)
                    case "-":
                        second_operand = st.pop()
                        first_operand = st.pop()
                        st.append(first_operand  -  second_operand)
                    case '*':
                        second_operand = st.pop()
                        first_operand = st.pop()
                        st.append(first_operand * second_operand)
                    case '/':
                        second_operand = st.pop()
                        first_operand = st.pop()
                        num = first_operand //second_operand
                        if num <= 0:
                            num = math.ceil(first_operand /second_operand)
                            st.append(num)
                        else:
                            st.append(first_operand //second_operand)
        return st.pop()
sol = Solution()
ex = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(f"Output: {sol.evalRPN(ex)}")




