class Vehicle:
	def __init__(self,regno,age):
		self.age =  age
		self.regno = regno

class Car(Vehicle):

	def __init__(self,regno,age):
		Vehicle.__init__(self,regno,age)

	def getType(self):
		return "Car"
