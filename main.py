import itertools

def findFuel(val) :
    fuel = 0

    while True :
        val = int(val / 3) - 2
        if val > 0 :
            fuel += val
        else :
            break

    return fuel 

def programLogic(inputs):
    TERMINATE = 99
    ADD = 1
    MULTIPLY = 2

    memory = inputs[:]

    for i, opcode in itertools.islice(enumerate(memory), 0, None, 4):
        operation = None

        if opcode == ADD:
            operation = lambda pos1, pos2 : pos1 + pos2

        elif opcode == MULTIPLY:
            operation = lambda pos1, pos2 : pos1 * pos2

        elif opcode == TERMINATE:
            break

        else:
            raise Exception('Unidentified Opcode!')

        param1Pos = memory[i + 1]
        param2Pos = memory[i + 2]
        outputPos = memory[i + 3]

        memory[outputPos] = operation(memory[param1Pos], memory[param2Pos])

    return memory[0]

def part1(inputs) :
    inputs[1] = 12
    inputs[2] = 2

    try :
        result = programLogic(inputs)
        print('\nPart 1 Solution: ', result, '\n')

    except:
        print('Part 1 Solution: ERROR!')

def part2(inputs) :
    DESIRED = 19690720
    noun = verb = None
    for i in range(100) :
        for j in range(100) :
            inputs[1] = i 
            inputs[2] = j

            try :
                output = programLogic(inputs)

                if output == DESIRED :
                    noun = i
                    verb = j
                    break

            except :
                print('\nPart 2 Solution: ERROR!\n')

    result = 100 * noun + verb
    print('\nPart 2 Solution: ', result, '\n')


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

    with open('resources/input2.txt') as file2:
        inputs = [int(i) for i in file2.read().split(',')]

    part1(inputs)    
    part2(inputs)

