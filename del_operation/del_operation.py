# Miguel de la Cruz Cabello
# Chris Meritt
# COMS 326
# 7 February 2021
import timeit
import random

def delItems(self):
    index = random.randrange(len(self) -1)
    try:
        del self[index]
    except KeyError:
        self.setdefault(index, None)
        del self[index]

for i in range(10000,1000001,20000):
    t_list= timeit.Timer("del self[random.randrange(len(self)-1)]",
    "from __main__ import random, self")
    t_dictionary = timeit.Timer("delItems(self)", "from __main__ import random, self, delItems")
    self = list(range(i))
    lst_time = t_list.timeit(number=100)
    self = {j:None for j in range(i)}
    d_time = t_dictionary.timeit(number=100)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))

# As we can see, the performance time of the dictionary is faster. For the first elements,
# the list is faster than the dictionary. However, as the number of items is increasing,
# the dictionary becomes more faster than the list. This verifies the explanation that the contains
# operator on a list is O(n) as it grows moslty linear, and in the dictionary O(1), as it stays mostly 
# constant all the time
