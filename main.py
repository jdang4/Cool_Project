def findFuel(val) :
    fuel = 0

    while True :
        val = int(val / 3) - 2
        if val > 0 :
            fuel += val
        else :
            break

    return fuel 


if __name__ == '__main__':
    file = open("resources/input1.txt", "r")
    
    totalSum = 0
    totalFuelSum = 0
    
    for line in file :
        val = int(line)
        result = int(val / 3) - 2
        fuelRes = findFuel(val)
        totalSum += result 
        totalFuelSum += fuelRes 

    print(totalSum)
    print(totalFuelSum)