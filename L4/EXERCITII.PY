def eval_expr(expr):
    operands = []
    numbers = []
    number = 0
    prio = {
        '+': (1, lambda a, b: a + b),
        '-': (1, lambda a, b: a - b),
        '*': (2, lambda a, b: a * b),
        '/': (2, lambda a, b: a // b)
    }
    for char in expr:
        if char not in "0123456789":
            operands.append(char)
            numbers.append(number)
            number = 0
        else:
            number = number * 10 + int(char)
    numbers.append(number)
    for i in range(len(operands)):
        if operands[i] == '-':
            numbers[i + 1] = -numbers[i + 1]
            operands[i] = '+'

    while (len(numbers) > 2):
        op1 = operands[-1]
        op2 = operands[-2]
        if prio[op1][0] == prio[op2][0]:
            value = prio[op1][1](numbers[-1], numbers[-2])
            operands.pop(-1)
            numbers[-1] = value
            numbers.pop(-2)
        elif prio[op1][0] < prio[op2][0]:
            value = prio[op2][1](numbers[-3], numbers[-2])
            numbers[-2] = value
            numbers.pop(-3)
            operands.pop(-2)
        else:
            value = prio[op1][1](numbers[-1], numbers[-2])
            operands.pop(-1)
            numbers[-1] = value
            numbers.pop(-2)
    return prio[operands[0]][1](numbers[0], numbers[1])

print(eval('36/6+5*2-8-4-2*2*2+2'))
print(eval_expr('36/6+5*2-8-4-2*2*2+2'))
