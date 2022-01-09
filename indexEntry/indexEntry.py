import ADT

class IndexEntry:
    def __init_(self, key, page):
        self.Key = key
        self.PageNumber = page

    def __gt__(self, other):
        if other == None:
            return False
        else: 
            if type(other) is IndexEntry:
                return self.Key > other.Key
            else:
                return self.Key > other

    def __lt__(self, other):
        if other == None:
            return False
        else: 
            if type(other) is IndexEntry:
                return self.Key < other.Key
            else:
                return self.Key < other

    def __eq__(self, other):
        if other == None:
            return False
        else: 
            if type(other) is IndexEntry:
                return self.Key == other.Key
            else:
                return self.Key == other

i = ADT.BinarySearchTree()
entry = IndexEntry("frog", 112)
i.insert(entry)
entry = IndexEntry("cat", 72)
i.insert(entry)
entry = IndexEntry("bird", 542)
i.insert(entry)
entry = IndexEntry("dog", 16)
i.insert(entry)
entry = IndexEntry("turtle", 170)
i.insert(entry)
entry = IndexEntry("goat", 55)
i.insert(entry)

while True:
    term = input("Please enter a search term or 'q' to quit: ")
    if term == 'q':
        break
    elif term in i:
        print("'%s' is found on page %i" % (term, i[term].keyPageNumber))
    else:
        print("'%s' was not found." % (term))

