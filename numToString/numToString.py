import ADT

def numToString(n, base):
    charArray = "0123456789ABCDEF"
    return charArray[n % base] if n < base else numToString(n // base, base) + charArray[n % base]

rStack = ADT.Stack()
call = 0

def toStr(n, base):
    global call
    call += 1
    charArray = "0123456789ABCDEF"
    if n < base:
        rStack.push("Call: %i result = %s" % (call, charArray[n]))
    else:
        rStack.push("Call: %i result = %s" % (call, charArray[n % base]))
        toStr(n // base, base)

print(numToString(10, 2))
toStr(10, 2)
while not rStack.isEmpty():
    print(rStack.pop())