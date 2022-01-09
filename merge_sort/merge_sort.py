def MergeSort(values):
    print("Splitting", values)
    if len(values) > 1:
        midpoint = len(values) // 2
        left = values[0:midpoint]
        right = values[midpoint:]

        MergeSort(left)
        MergeSort(right)

        leftIndex = 0
        rightIndex = 0
        resultIndex = 0

        print("Merging", left, "with", right)
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                values[resultIndex] = left[leftIndex]
                leftIndex += 1
            else:
                values[resultIndex] = right[rightIndex]
                rightIndex += 1
            resultIndex += 1

        while leftIndex < len(left):
            values[resultIndex] = left[leftIndex]
            leftIndex += 1
            resultIndex += 1

        while rightIndex < len(right):
            values[resultIndex] = right[rightIndex]
            rightIndex += 1
            resultIndex += 1
    print("Result", l)
l = [8,12,20,45,72,3,9,68]
print(l)
MergeSort(l)
print(l)
