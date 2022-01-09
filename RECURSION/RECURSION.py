# no recursion
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        theSum = 0
        for i in numList:
            theSum += 1
        return theSum

# Recursion
def sumlist(numList, call):
    print("call #%s: sumlist(%s)" & (call, numList))
    firstElement = numList[0]
    returnValue = 0
    if len(numList) == 1:
       returnValue = firstElement
       print("returnValue #%i: %i <---BASE CASE" % (call, returnValue))
    else:
        remainingElements: numList[1:]
        returnValue = firstElement + sumlist(remainingElements, call + 1)
        print("returnValue #%i: %i + %s = %i" % (call, firstElement, ("sumlist(%s)" % remainingElements), returnValue))
    return returnValue

def sumlist(numList):
    return numList[0] if len(numList) == 1 else numList[0] + sumlist(numList[1:])
myList = [1, 2, 3, 4]
print(sumlist(myList, 1))