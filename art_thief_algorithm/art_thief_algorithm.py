
# Miguel de la Cruz Cabello
# Professor Merritt
# COMS 326
# 5 March 2021

def maxLoot(items, W, loot):
    if len(items) <= 1: # If the length of the list is less than 1, return the element
        return [items]
    l = []
    for i in range(len(items)):
        m = items[i]
        itemNumbers = []
        weightOfItems = 0
        valueOfItems = 0
        for item in items:
            valueOfItems += item[2] # Add the item's value item[2] to valueOfItems
            weightOfItems += item[1] # Add the item's value item[1] to weightOfItems
            if weightOfItems <= W:
                itemNumbers.append(item[0])
                if loot[0] < valueOfItems:
                    loot[0] = valueOfItems
                    loot[1] = weightOfItems
                    loot[2] = itemNumbers
        remaining = items[:i] + items[i+1:] # remaining list after extracting items[i] from the list
        for p in maxLoot(remaining, W, loot): # Generating all the permutations where m is the first element
            l.append([m] + p)
    return l

items = [(1,2,3), (2,3,4), (3,4,8), (4,5,8), (5,9,10)]
loot = [0, 0, []]
maxLoot(items, 20, loot)
print(loot)