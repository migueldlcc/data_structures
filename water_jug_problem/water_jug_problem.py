# Miguel de la Cruz Cabello
# Professor Merritt
# COMS 326
# 1 May 2021

class Jug():
    def __init__(self, jug_4_max, jug_3_max, jug_4, jug_3, gallons):
        self.jug_4_max = 4
        self.jug_3_max = 3
        self.jug_4 = 0
        self.jug_3 = 0
        self.gallons = 2

    def fill_jug_4(self):
        self.jug_4 = 4
        print ('(', self.jug_4, ',', self.jug_3, ')')

    def fill_jug_3(self):
        self.jug_3 = 3
        print ('(', self.jug_4, ',', self.jug_3, ')')

    def empty_jug_4(self):
        self.jug_4 = 0
        print ('(', self.jug_4, ',', self.jug_3, ')')

    def empty_jug_3(self):
        self.jug_3 = 0
        print ('(', self.jug_4, ',', self.jug_3, ')')

    def pour_from_jug_4_to_jug_3(self):
        while True:
            self.jug_4 = self.jug_4 - 1
            self.jug_3 = self.jug_3 + 1
            if (self.jug_4 == 0 or self.jug_3 == 3):
                break
        print ('(', self.jug_4, ',', self.jug_3, ')')

    def main(self):
        while True:
            if (self.jug_4 == self.gallons or self.jug_3 == self.gallons):
                break
            if (self.jug_4 == 0):
                self.fill_jug_4()
            elif (self.jug_4 > 0 and self.jug_3 != 3):
                self.pour_from_jug_4_to_jug_3()
            elif (self.jug_4 > 0 and self.jug_3 == 3):
                self.empty_jug_3()

p= Jug(4,3,0,0,2)
p.main()
