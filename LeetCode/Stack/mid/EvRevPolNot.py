class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for item in tokens:
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
                        num = first_operand / second_operand
                        if num <= 0:
                            num = math.ceil(first_operand /second_operand)
                            st.append(num)
                        else:
                            st.append(first_operand //second_operand)
        return st.pop()