# Miguel de la Cruz Cabello
# Professor Meritt
# COMS 326
# 31 January 2021

# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
           
        m = old_n
        n = old_m % old_n
    return n

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        if bottom == 0:
            raise ZeroDivisionError("The denominator cannot be zero")

        # The built-in isinstance() function chacks the type of object referenced by a variable
        # I found this function in the Python Documentation website under built-in functions
        # https://docs.python.org/3/library/functions.html
        if not isinstance (top, int) or not isinstance(bottom, int):
            raise TypeError("The top and bottom parts of the fraction must be integers.")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
        self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        
        return first_num == second_num

y = Fraction(1, 2)
print("Valid fraction: ", y)

z = Fraction ('turtle', 4)
print("Invalid fraction: ", z)

t = Fraction ('a', 'b')
print("Invalid fraction: ", t)

x = Fraction(1, 'a')
print ("Invalid fraction:", x)

p = Fraction(1, 0)
print("Invalid fraction: ", p)


