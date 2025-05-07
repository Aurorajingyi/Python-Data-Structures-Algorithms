"""逆波兰式"""

# 定义运算符优先级
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2 # 优先级高
    return 0 # 其他没有运算符的，返回0（最低）

# 中缀表达式转后缀表达式（逆波兰式）
# 例子：2 * (3 + 4) 转为 2 3 4 + *
def infix_to_postfix(expression):
    output = []  # 输出的后缀表达式
    stack = []   # 运算符栈，帮助处理运算符的优先级
    number = ''  # 暂存数字字符串
    i = 0        # 当前遍历的位置

    while i < len(expression):
        ch = expression[i] # ch是每次遍历的当前字符
        if ch.isdigit() or ch == '.': # 循环几次得到一个小数
            # 数字或小数点，拼接成一个完整数字
            number += ch
            i += 1
        elif ch == '-' and (i == 0 or expression[i-1] in '(-+*/'):
            # 判断当前的 - 是否是负号，而不是减号运算符
            # 处理负号的情况（负数识别）
            number += ch
            i += 1
        else:
            if number:
                # 遇到非数字字符时，前面的数字整体加入输出
                output.append(number)
                number = ''
            if ch == '(':
                # 左括号直接入栈
                stack.append(ch)
            elif ch == ')':
                # 右括号，弹出直到遇到左括号
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # 弹出'('
            elif ch in '+-*/':
                # 运算符处理，弹出所有优先级更高或相同的运算符
                while stack and precedence(stack[-1]) >= precedence(ch):
                    output.append(stack.pop())
                stack.append(ch)
            i += 1

    if number:
        # 表达式结束时，如果还有未加入的数字
        output.append(number)

    # 把栈中剩余的运算符弹出
    while stack:
        output.append(stack.pop())

    return output

# 计算后缀表达式的结果
def evaluate_postfix(postfix_expr):
    stack = []
    for token in postfix_expr:
        if token.replace('.', '', 1).replace('-', '', 1).isdigit():
            # 数字直接入栈
            stack.append(float(token))
        else:
            # 运算符，弹出两个操作数进行计算
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

# 示例1
expr = "2*(-3.5+4.2)"
postfix = infix_to_postfix(expr)
print("中缀表达式:", expr)
print("后缀表达式:", ' '.join(postfix))
print("计算结果:", evaluate_postfix(postfix))

# 示例2 更复杂的表达式
expr2 = "-2*(9+6.0/3-5)+4"
postfix2 = infix_to_postfix(expr2)
print("中缀表达式:", expr2)
print("后缀表达式:", ' '.join(postfix2))
print("计算结果:", evaluate_postfix(postfix2))
