import Vehicle
import sys
import argparse


class ParkingLot:
	def __init__(self):
		self.capacity = 0
		self.slotid = 0
		self.numOfOccupiedSlots = 0

        #Create Parking Area
	def createParking(self,capacity):
		self.slots = [-1] * capacity
		self.capacity = capacity
		return self.capacity

        #Get empty area
	def getEmptySlot(self):
		for i in range(len(self.slots)):
			if self.slots[i] == -1:
				return i

	#Park vehicle with given slot numbers
	def park(self,regno,age):
		if self.numOfOccupiedSlots < self.capacity: 
			slotid = self.getEmptySlot()
			self.slots[slotid] = Vehicle.Car(regno,age)
			self.slotid = self.slotid+1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
			return slotid+1
		else:
			return -1

	#Empty the slot
	def leave(self,slotid):

		if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
			self.slots[slotid-1] = -1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
			return True
		else:
			return False

        
        #Retrieve Vin Number from Driver's age
	def getRegNoFromAge(self,age):

		regnos = []
		for i in self.slots:

			if i == -1:
				continue
			if i.age == age:
				regnos.append(i.regno)
		return regnos

	#Retrieve slot number from Vin Number			
	def getSlotNoFromRegNo(self,regno):
		
		for i in range(len(self.slots)):
			if self.slots[i].regno == regno:
				return i+1
			else:
				continue
		return -1
			

        #Retrieve slot number from Driver's Age
	def getSlotNoFromAge(self,age):
		
		slotnos = []

		for i in range(len(self.slots)):

			if self.slots[i] == -1:
				continue
			if self.slots[i].age == age:
				slotnos.append(str(i+1))
		return slotnos

        #Main working
	def show(self,line):
		if line.startswith('Create_parking_lot'):
			n = int(line.split(' ')[1])
			res = self.createParking(n)
			print('Created parking of '+str(res)+' slots')

		elif line.startswith('Park'):
			regno = line.split(' ')[1]
			age = line.split(' ')[3]
			res = self.park(regno,age)
			if res == -1:
				print("PARKING FULL!!!")
			else:
				print('Car with vehicle registration number "'+str(regno)+'" has been parked at slot number '+str(res))

		elif line.startswith('Leave'):
			leave_slotid = int(line.split(' ')[1])
			status = self.leave(leave_slotid)
			if status:
				print('Slot number '+str(leave_slotid)+' vacated, the car left the space')

		elif line.startswith('Vehicle_registration_number_for_driver_of_age'):
			age = line.split(' ')[1]
			regnos = self.getRegNoFromAge(age)
			print(', '.join(regnos))

		elif line.startswith('Slot_numbers_for_driver_of_age'):
			age = line.split(' ')[1]
			slotnos = self.getSlotNoFromAge(age)
			print(','.join(slotnos))

		elif line.startswith('Slot_number_for_car_with_number'):
			regno = line.split(' ')[1]
			slotno = self.getSlotNoFromRegNo(regno)
			if slotno == -1:
				print("Not found")
			else:
				print(slotno)
		elif line.startswith('exit'):
			exit(0)

#Input for Python 2.xx, if you're still using it
if sys.version_info[0] == 2:
	input = raw_input

def main():

	parkinglot = ParkingLot()
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input")
	args = parser.parse_args()
	
	if args.src_file:
		with open(args.src_file) as f:
			for line in f:
				line = line.rstrip('\n')
				parkinglot.show(line)
	else:
			while True:
				line = input("$ ")
				parkinglot.show(line)

if __name__ == '__main__':
	main()
