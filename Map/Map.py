
class Map():
    def hash(self, key):
        i = 0
        for char in str(key):
            i = i + ord(char)
        return i % self.size
    
    def put(self, key, value):
        slot = self.hash(key)
        keySublist = self.keyList[slot]
        valueSublist = self.valueList[slot]
        if keySublist == None:
            self.keyList[slot] = []
            self.valueList[slot] = []
        if key not in self.keyList[slot]:
            self.keyList[slot].append(key)
            self.valueList[slot].append(value)

    def get(self, key):
        slot = self.hash(key)
        keySublist = self.keyList[slot]
        if keySublist == None or key not in keySublist:
            return None
        position = ketSublist.index(key)
        return valueSublist[position]

    def keys(self):
        returnList = []
        for sublist in self.keyList:
            if sublist != None:
                returnList.extend(sublist)
        return returnList

    def values(self):
        returnList = []
        for sublist in self.valueList:
            if sublist != None:
                returnList.extend(sublist)
        return returnList

    def len(self):
        return len(self.keys()) 


m = Map()
m.put("cat", "meow")
m.put
