class Chooser:

    def __init__(self):
        self.name = "Chooser"
        self.fileName = ""

    def set_file_name(self, name):
        self.fileName = name

    def findFuel(self, val) :
        fuel = 0
        
        while True :
            val = int(val / 3) - 2
            
            if val > 0 :
                fuel += val
            else :
                break

        return fuel

    def function1(self):
        file = open(self.fileName, "r")
        
        totalSum = 0
        totalFuelSum = 0
        
        for line in file :
            val = int(line)
            result = int(val / 3) - 2
            fuelRes = self.findFuel(val)
            totalSum += result 
            totalFuelSum += fuelRes 

        print(totalSum)
        print(totalFuelSum)