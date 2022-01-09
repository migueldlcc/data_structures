import Examples
f = Examples.Fraction(1, 4)
g = Examples.Fraction(1, 2)

print (f + g)
print (f == g)

import LogicGates
g1 = LogicGates.AndGate("G1")
x = g1.getOutput()
print(x)
