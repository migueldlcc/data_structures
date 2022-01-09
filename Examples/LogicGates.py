class LogicGate:
	def __init__(self, n):
		self.label = str(n)
		self.output = None

	def getOutput(self):
		self.output = self.perfomGateLogic()
		return self.output

class BinaryGate(LogicGate):
	def __init__(self, n):
		super().__init__(n)
		self.PinA = None
		self.PinB = None

	def getPinA(self):
		return int(input("Enter PinA input for gate %s --> " % (self.label)))

	def getPinB(self):
		return int(input("Enter PinB input for gate %s --> " % (self.label)))

class UnaryGate(LogicGate):
	def __init__(self, n):
		super().__init__(n)

	def getPinA(self):
		return int(input("Enter Pin input for gate %s --> " % (self.label)))

class AndGate(BinaryGate):
	def __init__(self, n):
		super().__init__(n)

	def perfomGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if (a == 1 and b == 1):
			return 1
		else:
			return 0


