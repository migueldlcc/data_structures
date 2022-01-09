def mergeSort(values):
    if len(values) > 1:
        midpoint = len(values) // 2
        left: values[0:midpoint]
        right = values[midpoint:]

        mergeSort(left)
        mergeSort(right)

        leftIndex = 0
        rightIndex = 0
        resultIndex = 0

        while (leftIndex < len(left) and rightIndex < len(right)):
            if (left[leftIndex] < right[rightIndex]):
                values [resultIndex] = left[leftIndex]
                leftIndex += 1
            else:
                values [resultIndex] = right[rightIndex]
                rightIndex += 1
            resultIndex += 1

        while leftIndex < len(left):
            values [resultIndex] = left[leftIndex]
            leftIndex += 1
            resultIndex += 1
        while leftIndex < len(left) and 
                values [resultIndex] = left[leftIndex]
                leftIndex += 1
                resultIndex += 1