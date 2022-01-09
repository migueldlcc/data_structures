class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def insert(self, k):
        self .heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                self.heaplist[i // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[i // 2]
            i = i // 2

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2

            else:
                return i * 2 + 1

    def build (self, valueList):
        i = len(valueList) // 2
        self.currentSize = len(valueList)
        self.heaplist = [0] + valueList[:]
        while i > 0:
            self.percDown(i)
            i -= 1

l = [21,13,12,19,24,7,3,22,16,4,9,18]
h = BinaryHeap()
h.build(l)
print(h.heaplist)