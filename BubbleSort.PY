# Miguel de la Cruz Cabello
# Professor Merritt
# COMS 326
# 28 March 2021

def BubbleSort(items):
    for passnum in range(len(items) - 1, 0, -1):
        changes = False
        for i in range(passnum):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                changes = True
            if items[len(items) - (i + 1)] < items[len(items) - (i + 2)]:
                items[len(items) - (i + 1)], items[len(items) - (i + 2)] = items[len(items) - (i + 2)], items[len(items) - (i + 1)]
                changes = True
        if not changes:
            break


arr_list= [3,17,24,2,6,10,11,38,20,58,83,49]
print(arr_list)
BubbleSort(arr_list)
print(arr_list)

