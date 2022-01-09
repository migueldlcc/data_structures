class HashTable:
    def __init__(self):
        self.size = 11
        self.data = [None] * self.size # Creating a list of size 11 and each of those slots is initialized with the value None

    def hash(self, value):
        return value % self.size

    def put(self, value):
        hashValue = self.hash(value)
        if self.data[hashValue] == None:
            self.data[hashValue] = []
        if value not in self.data[hashValue]:
            self.data[hashValue].append(value)

    def __str__(self):
        output = []
        for sublist in self.data:
            if sublist != None:
                output.extend(sublist)
        return str(output)

    def __contains__(self, value):
        hashValue = self.hash(value)
        if self.data[hashValue] == None:
            return False
        else:
            return value in self.data[hashValue]

    def __getitem__(self, index):
        output = []
        for sublist in self.data:
            if sublist != None:
                 output.extend(sublist)
        try:
            return output
        except:
            return None


h = HashTable()
h.put(11)
h.put(26)

b = 34 in h
print(b)


       