# Miguel de la Cruz Cabello
# Professor Merritt
# COMS 326
# 21 March 2021

loopcount = 0
# LinearSearch is O(n).
# LinearSearch simply compares every element in a list with
# the search value until the value is found (in which case it
# returns True), or the end of the list is reached (in which
# case it returns False).
def LinearSearch(items, value):
    global loopcount
   
    for item in items:
        loopcount += 1 # Increments the counter
        if item == value:
            return True
    return False
# BinarySearch is O(log n).
# BinarySearch only works when the items in the list are sorted.
# For unsorted lists you could consider using a sort algorithm
# such as MergeSort prior to executing BinarySearch.

def BinarySearch(items, value):
    global loopcount
   

    if len(items) == 0 or len(items) == 1 and items[0] != value:
        return False
    else:
        # Find the value of the element in the middle of the list.
        middle = len(items) // 2
        middleValue = items[middle]
        # If the value in the middle of the list is greater than
        # the value being searched, recursively search the left
        # half of the list.
        if middleValue > value:
            loopcount += 1 # If the value is greater than the middlevalue, we know our value has to be on the left half. Repeat the same process of slpitting into halves to find the value
            partialList = items[:middle]
            return BinarySearch(partialList, value)
        # If the value in the middle of the list is less than
        # the value being searched, recursively search the right
        # half of the list.
        elif middleValue < value:
            loopcount += 1 # If the value is greater than the middlevalue, we know our value has to be on the right half. Repeat the same process of slpitting into halves to find the value
            partialList = items[-1 * middle:]
            return BinarySearch(partialList, value)
        # If the value in the middle matches the value being searched
        # then return True.
        elif middleValue == value:
            return True
    # If you we make it to here then the value does not exist in the list.
    return False

loopcount = 0
l = [1,5,7,9,10,24,37,41,48,54,63,76,89]
print(LinearSearch(l,41))
print("Number of iterations for linear search: ", loopcount)
loopcount = 0
print(BinarySearch(l, 41))
print("Number of iterations for binary search: ", loopcount)
loopcount = 0
print(LinearSearch(l, 63))
print("Number of iterations linear search: ", loopcount)
loopcount = 0
print(BinarySearch(l, 63))
print("Number of iterations binary search: ", loopcount)
loopcount = 0
print(LinearSearch(l, 1))
print("Number of iterations linear search: ", loopcount)
loopcount = 0
print(BinarySearch(l, 1))
print("Number of iterations for binary search: ", loopcount)
 
