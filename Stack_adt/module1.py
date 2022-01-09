import Stack_adt

s = Stack_adt()
s.push(2)

def balanced(string):
    s = Stack_adt.Stack()
    bal = True
    index = 0
    while index < len(string) and bal:
        symbol = string[index]
        if symbol in {"(", "[", "{"}:
            s.push(symbol)
        else:
            if s.isEmpty():
                bal = False
            else:
                top = s.pop()
                bal = (top == "(" and symbol == ")") or (top == "[" and symbol == "]") or (top == "{" and symbol == "}")

def DecToBin(decimalValue):
    if decimalValue < 1:
        return 0
    stack = Stack_adt.Stack()
    while decimalValue > 0:
        remainder = decimalValue % 2
        stack.push(remainder)
        decimalValue = decimalValue // 2
    binaryString = ""
    while not stack.isEmpty():
        binaryString += str(stack.pop)

