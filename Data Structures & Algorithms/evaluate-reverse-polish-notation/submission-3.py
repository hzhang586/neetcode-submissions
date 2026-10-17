class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}

        ans = 0
        num_stack = []

        if len(tokens) == 1:
            return int(tokens[-1])

        for i,x in enumerate(tokens):

            if x in operators:
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                if x == "+":
                    ans = (num2+num1)
                elif x == "-":
                    ans = (num2-num1)
                elif x == "*":
                    ans = (num2 * num1)
                elif x == "/":
                    ans = int(num2 / num1)
                
                num_stack.append(ans)
            else:
                num_stack.append(int(x))
            
        
        return ans




        