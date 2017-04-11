#import serial
import time

class reading(): #reading object, used to organise data and calculate
                 #an overall weight estimate from the readings of
                 #the three pressure sensors, and generate a JSON object

    def __init__(self, backLeft, backRight, front):
        self.timestamp = str(int(time.time())) #saves time of reading
        self.backLeft = backLeft
        self.backRight = backRight
        self.front = front
        self.weightEstimate = backLeft + backRight + front #weightEstimate is
                                                           #sum of all readings
    def __str__(self):
        str_bl = str(self.backLeft)
        str_br = str(self.backRight)
        str_fr = str(self.front)
        return self.timestamp+":["+str_bl+","+str_br+","+str_fr+"]"
        
weightThreshHold = 20 #minimum reading for toilet to be considered sat on
lengthThreshHold = 3
poopEvent = [] #list recording weights of current toilet sit

while 1:
    backLeft = float(input("Enter mock bl: "))
    backRight = float(input("Enter mock br: "))
    front = float(input("Enter mock front: "))

    currentReading = reading(backLeft, backRight, front) #creats reading object
                                                         #from 3 readings 
    
    if currentReading.weightEstimate >= weightThreshHold: 
        poopEvent.append(str(currentReading))

    elif len(poopEvent):
        if len(poopEvent) >= lengthThreshHold:
            print(poopEvent)
        poopEvent = []
