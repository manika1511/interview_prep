def postfix_to_infix(expression):
    stack = []
    result = ""
    for i in range(0, len(expression)):
        if expression[i] != '+' and expression[i] != '-' and expression[i] != '/' and expression[i] != '*' and \
                        expression[i] != '^' and expression[i] != " ":
            stack.append(expression[i])
        elif expression[i] == "+" or expression[i] == '-' or expression[i] == '/' or expression[i] == '*' or \
                        expression[i] == '^':
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                if len(x) > 1:
                    x = "(" + x + ")"
                if len(y) > 1:
                    y = "(" + y + ")"
                result = y + expression[i] + x
                stack.append(result)
    if len(stack) == 1:
        s = stack.pop()
        # return s[1:len(s)-1]
        return s



def postfix_to_infix(expression):
    stack = []
    result = ""
    for i in range(0, len(expression)):
        if expression[i] != '+' and expression[i] != '-' and expression[i] != '/' and expression[i] != '*' and \
                        expression[i] != '^' and expression[i] != " ":
            stack.append(expression[i])
        elif expression[i] == "+" or expression[i] == '-' or expression[i] == '/' or expression[i] == '*' or \
                        expression[i] == '^':
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                result = y + expression[i] + x
                result = "(" + result + ")"
                stack.append(result)
    if len(stack) == 1:
        s = stack.pop()
        return s[1:len(s)-1]

print (postfix_to_infix("abc-+de-fg-h+/*"))