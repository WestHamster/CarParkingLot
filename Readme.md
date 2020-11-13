# Parking Lot System

Design a Parking Lot for 'n' number of cars.

## 🌱 Dependencies

Python 2.xx or Python 3.xx - https://www.python.org/downloads/

## 🔭 Description

1. Create a parking lot with given input and store -1 in all the slot, showing empty space available.
2. Store the car registration number and age into slots
   2.1. If slot is empty, fill the place
   2.2.  If slot is not empty find the next empty slot nearby
3. To retrieve the queries stated in the Input file, use ‘startswith’ method in
python and use ‘==’ operator or string 4/match to find the required information

4. To leave the slot, find the slot number to be left and remove the slot from occupied slot to -1
To exit the system, enter ‘exit’

> Functions

1. __init__ : constructor to allot the variables
2. createParking : create parking space with given n size
3. getEmptySlot : check if the slot is empty or not
4. park: obtain the vehicle registration number and driver’s age into the slot
5. leave: clear the slot with given number
6. getRegNoFromAge: find the registration number of car with the given age input
7. getSlotNoFromRegNo: find the slot number using vehicle registration number
8. getSlotNoFromAge: find the slot number using driver’s age
9. show : to obtain the queries from the input file and return output

> How to Run?

1. Clone the repository
2. Run the command “python parkingLot.py” and give the input.
3. Run the command “python parkingLot.py -f input.txt” with input file 







[For complete documentation](shorturl.at/dils7)
