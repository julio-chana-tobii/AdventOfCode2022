#import common libraries
import os
import sys
import time
import math
class Directory:
    def __init__(self, name, parent, isDir=True, size=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = size
        self.isDir = isDir
    def add_child(self, child):
        self.children.append(child)
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    def get_path(self):
        path = self.name
        parent = self.parent
        while parent != None:
            path = parent.name + "/" + path
            parent = parent.parent
        return path
    def get_children(self):
        return self.children
    def get_name(self):
        return self.name
    def get_parent(self):
        return self.parent
    def get_size(self):
        #i fit is a directory, get the size of all children
        if self.isDir:
            size = 0
            for child in self.children:
                size += child.get_size()
            return size
        else:
            return self.size
    def is_dir(self):
        return self.isDir
    def __str__(self):
        return self.name
def GetRecursiveSmallSizeSum(directory):
    sum=0
    if(directory.is_dir()):
        if directory.get_size()<=100000:
            sum+=directory.get_size()
    for child in directory.get_children():
        if child.is_dir():
            sum+=GetRecursiveSmallSizeSum(child)

    return sum
def FindSmallestBigEnoughFileSize(directory, requieredSize, currentSize):
    if directory.is_dir():
        #first check if the folder itself is big enough
        if directory.get_size()>=requieredSize:
            #check if it is smaller than the current selected size
            if directory.get_size()<currentSize:
                currentSize = directory.get_size()
        #check if any of the children are big enough
        for child in directory.get_children():
            currentSize = FindSmallestBigEnoughFileSize(child, requieredSize, currentSize)
    return currentSize
def December7P1(real_data):
    #read input file
    if real_data == True:
        input_file = open("Devember7Input", "r")
    else:
        input_file = open("testInput", "r")
    input_data = input_file.read()
    input_file.close()
    #split input into lines
    headDirectory = Directory("root", None)
    currentDirectory = headDirectory
    input_data = input_data.splitlines()
    for line in input_data:
        if "$" in line:
            #split by spaces
            line = line.split(" ")
            if line[1] == "cd" :
                if line[2] == "/":
                    currentDirectory = headDirectory
                elif line[2] == "..":
                    if currentDirectory.get_parent() != None:
                        currentDirectory = currentDirectory.get_parent()
                    else:
                        print("cannot move back")
                else:
                    print("move forward command to " + line[2])
                    #check if directory exists
                    child = currentDirectory.get_child(line[2])
                    if child != None:
                        currentDirectory = child
                    else:
                        print("directory "+ line[2] +" does not exist")
            elif line[1] == "ls":
                print("list command")

        elif "dir" in line:
            #print("dir")
            #split by spaces
            line = line.split(" ")
            #check if directory exists
            child = currentDirectory.get_child(line[1])
            if child != None:
                print("directory "+ line[1] +" already exists")
            else:
                #create directory
                newDirectory = Directory(line[1], currentDirectory)
                currentDirectory.add_child(newDirectory)
                print("directory "+ line[1] +" created")
        else: #file
            #split by spaces
            line = line.split(" ")
            #check if directory exists
            child = currentDirectory.get_child(line[1])
            if child != None:
                print("file "+ line[1] +" already exists")
            else:
                #create file
                newFile = Directory(line[1], currentDirectory, False, int(line[0]))
                currentDirectory.add_child(newFile)
                print("file "+ line[1] +" created")
            # if(int(line[0])<=100000):
            #     sum+=int(line[0])
            #     print(line[0])
            pass

    sum=0
    sum= GetRecursiveSmallSizeSum(headDirectory)
    print(sum)

def December7P2(real_data):
     #read input file
    if real_data == True:
        input_file = open("Devember7Input", "r")
    else:
        input_file = open("testInput", "r")
    input_data = input_file.read()
    input_file.close()
    #split input into lines
    headDirectory = Directory("root", None)
    currentDirectory = headDirectory
    input_data = input_data.splitlines()
    for line in input_data:
        if "$" in line:
            #split by spaces
            line = line.split(" ")
            if line[1] == "cd" :
                if line[2] == "/":
                    currentDirectory = headDirectory
                elif line[2] == "..":
                    if currentDirectory.get_parent() != None:
                        currentDirectory = currentDirectory.get_parent()
                    else:
                        print("cannot move back")
                else:
                    print("move forward command to " + line[2])
                    #check if directory exists
                    child = currentDirectory.get_child(line[2])
                    if child != None:
                        currentDirectory = child
                    else:
                        print("directory "+ line[2] +" does not exist")
            elif line[1] == "ls":
                print("list command")

        elif "dir" in line:
            #print("dir")
            #split by spaces
            line = line.split(" ")
            #check if directory exists
            child = currentDirectory.get_child(line[1])
            if child != None:
                print("directory "+ line[1] +" already exists")
            else:
                #create directory
                newDirectory = Directory(line[1], currentDirectory)
                currentDirectory.add_child(newDirectory)
                print("directory "+ line[1] +" created")
        else: #file
            #split by spaces
            line = line.split(" ")
            #check if directory exists
            child = currentDirectory.get_child(line[1])
            if child != None:
                print("file "+ line[1] +" already exists")
            else:
                #create file
                newFile = Directory(line[1], currentDirectory, False, int(line[0]))
                currentDirectory.add_child(newFile)
                print("file "+ line[1] +" created")
            # if(int(line[0])<=100000):
            #     sum+=int(line[0])
            #     print(line[0])
            pass
    totalMemory=70000000
    neededMemory=30000000
    currentlyusedMemory=headDirectory.get_size()
    print("currently used memry: " + str(currentlyusedMemory))
    remainingMemory=totalMemory-currentlyusedMemory
    print("remaining memory: " + str(remainingMemory))
    requieredMemory=neededMemory-remainingMemory
    print("requiered memory: " + str(requieredMemory))
    if requieredMemory>0:
        print("not enough memory")
        print(FindSmallestBigEnoughFileSize(headDirectory, requieredMemory,currentlyusedMemory))

#December7P1(True)
#December7P2(True)

def December8p1(realData):
    #first readd the data
    if realData == True:
        input_file = open("December8Input.txt", "r")
    else:
        input_file = open("testInput", "r")
    input_data = input_file.read()
    input_file.close()
    treeHeightArray = []
    treeVisibilityArray = []

    treeRows = input_data.splitlines()
    for x in range (0, len(treeRows)):
        treeHeightRow = []
        visibilityRow = []
        for y in range (0, len(treeRows[x])):
            treeHeightRow.append(int(treeRows[x][y]))
            visibilityRow.append(False)
        treeHeightArray.append(treeHeightRow)
        treeVisibilityArray.append(visibilityRow)
    #look horizontally
    for x in range(0, len(treeHeightArray)):
        tallestTree = -1
        for y in range(0, len(treeHeightArray[x])):
            if treeHeightArray[x][y] > tallestTree:
                tallestTree = treeHeightArray[x][y]
                treeVisibilityArray[x][y] = True
            else:
                pass
    for x in range(0, len(treeHeightArray)):
        tallestTree = -1
        for y in range(1, len(treeHeightArray[x])):
            if treeHeightArray[x][-y] > tallestTree:
                tallestTree = treeHeightArray[x][-y]
                treeVisibilityArray[x][-y] = True
            else:
                pass
    #look vertically
    for y in range(0, len(treeHeightArray[0])):
        tallestTree = -1
        for x in range(0, len(treeHeightArray)):
            if treeHeightArray[x][y] > tallestTree:
                tallestTree = treeHeightArray[x][y]
                treeVisibilityArray[x][y] = True
            else:
                pass
    for y in range(0, len(treeHeightArray[0])):
        tallestTree = -1
        for x in range(1, len(treeHeightArray)):
            if(treeHeightArray[-x][y] > tallestTree):
                tallestTree = treeHeightArray[-x][y]
                treeVisibilityArray[-x][y] = True
            else:
                pass
    #count visible trees
    count =0
    for x in range(0, len(treeVisibilityArray)):
        for y in range(0, len(treeVisibilityArray[x])):
            if treeVisibilityArray[x][y] == True:
                count+=1

    print("there are " + str(count) + " visible trees")

def CalculateScenicViewScore(x, y, treeHeightArray):

    northScore = 0
    southScore = 0
    eastScore = 0
    westScore = 0


    #look north
    for i in range(1, x+1):
        if treeHeightArray[x-i][y] < treeHeightArray[x][y]:
            northScore+=1
        else :
            northScore+=1
            break

    #look south
    for i in range(1, len(treeHeightArray)-x):
        if treeHeightArray[x+i][y] < treeHeightArray[x][y]:
            southScore+=1
        else :
            southScore+=1
            break

    #look east
    for i in range(1, len(treeHeightArray[x])-y):
        if treeHeightArray[x][y+i] < treeHeightArray[x][y]:
            eastScore+=1
        else:
            eastScore+=1
            break

    #look west
    for i in range(1, y+1):
        if treeHeightArray[x][y-i] < treeHeightArray[x][y]:
            westScore+=1
        else:
            westScore+=1
            break

    return northScore *southScore *eastScore *westScore

def December8p2(realData):

    treeHeightArray = []
    scenicViewScoreArray = []

    treeRows = input_data.splitlines()
    for x in range (0, len(treeRows)):
        treeHeightRow = []
        scenicScoreRow = []
        for y in range (0, len(treeRows[x])):
            treeHeightRow.append(int(treeRows[x][y]))
            scenicScoreRow.append(0)
        treeHeightArray.append(treeHeightRow)
        scenicViewScoreArray.append(scenicScoreRow)
        #foreach tree
    highest = 0
    for x in range(0, len(treeHeightArray)):
            for y in range(0, len(treeHeightArray[x])):
                scenicViewScoreArray[x][y] = CalculateScenicViewScore(x, y, treeHeightArray)
                if(scenicViewScoreArray[x][y] > highest):
                    highest = scenicViewScoreArray[x][y]
    print (highest)
    # print(treeHeightArray)
    # print(scenicViewScoreArray)
#December8p2(True)
def December10p1(lines):
    cycles = 1
    x_value = 1
    signal_strength_sum = 0
    for line in lines:
        line =line.split(" ")
        if line[0] == "noop":
            if (cycles +20) %40 ==0:
                print("x: " + str(x_value)+ " in cycle " + str(cycles))
                signal_strength_sum+=(x_value*cycles)
            cycles+=1

        elif line[0] == "addx":
            for i in range(0, 2):
                if (cycles +20) %40 ==0:
                    print("x is " + str(x_value) + " in cycle " + str(cycles))
                    signal_strength_sum+=(x_value*cycles)

                cycles+=1
            x_value+=int(line[1])

    print(signal_strength_sum)
    pass
def December10p2(lines):
    cycles = 0
    x_value = 1
    output=""
    for line in lines:
        line =line.split(" ")
        if line[0] == "noop":
            if (cycles%40)-x_value>1 or (cycles%40)-x_value<-1:
                output+=str(" ")
            else:
                output+=str("#")
            if (cycles%40)==0:
                #add a break line
                print(output)
                output=""
            cycles+=1

        elif line[0] == "addx":
            for i in range(0, 2):
                if (cycles%40)-x_value>1 or (cycles%40)-x_value<-1:
                    output+=str(" ")
                else:
                    output+=str("#")
                if (cycles%40)==0:
                    #add a break line
                    print(output)
                    output=""


                cycles+=1
            x_value+=int(line[1])
    print(output)
    pass

worryLevelMagicNumber=1

class Monkey:
    items = []
    operand1 = ""
    operandSign = ""
    operand2 = ""
    divisionNumber = 0
    trueThrow = 0
    falseThrow = 0
    monkeyBussiness = 0
    def __init__(self, operand1, operand2,operationSign, divisionNumber, trueThrow, falseThrow, items):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operandSign = operationSign
        self.divisionNumber = divisionNumber
        self.trueThrow = trueThrow
        self.falseThrow = falseThrow
        self.items = items

    def operate(self, monkeyList):
        #for each item in the list
        # while the monkey has items
        while len(self.items) > 0:
            worryLevel = int(self.items[0])
            self.items.remove(self.items[0])
            self.monkeyBussiness +=1
            #first inspect each item
            if self.operand1 =="old":
                firstOperand = int(worryLevel)
            else:
                firstOperand = int(self.operand1)

            if self.operand2 =="old":
                secondOperand = int(worryLevel)
            else:
                secondOperand = int(self.operand2)

            if self.operandSign =="+":
                worryLevel = firstOperand + secondOperand
            elif self.operandSign =="-":
                worryLevel = firstOperand - secondOperand
            elif self.operandSign =="*":
                worryLevel = firstOperand * secondOperand
            elif self.operandSign =="/":
                worryLevel = firstOperand / secondOperand
            #worryLevel = worryLevel / 3
            # round to the floor
            worryLevel = math.floor(worryLevel)
            global worryLevelMagicNumber
            if worryLevelMagicNumber%self.divisionNumber==0:
                pass
            else:
                print("magic number is " + str(worryLevelMagicNumber) + " and division number is " + str(self.divisionNumber))

            if(worryLevel > worryLevelMagicNumber):
                worryLevel-= worryLevelMagicNumber * math.floor( worryLevel/worryLevelMagicNumber)
            #now evaluate the item
            if(worryLevel % self.divisionNumber == 0):
                #throw true
                monkeyList[self.trueThrow].items.append(worryLevel)
            else:
                monkeyList[self.falseThrow].items.append(worryLevel)


        pass
def December11P1(lines):
    # first build the monkey list
    monkeyList = []
    currentItemList = []
    currentOperationSign = ""
    currentOperator1 = ""
    currentOperator2 = ""
    currentDivisionNumber = 0
    currentTrueThrow = 0
    currentFalseThrow = 0

    for line in lines:

        line = line.split(" ")
        print (line)
        if(len(line) == 1):
            monkeyList.append(Monkey(currentOperator1, currentOperator2, currentOperationSign, currentDivisionNumber, currentTrueThrow, currentFalseThrow, currentItemList))
        elif(line[0] == "Monkey"):
            currentItemList= []
            currentOperationSign = ""
            currenntOperator1 = ""
            currentOperator2 = ""
            currentDivisionNumber  = 0
            currentTrueThrow      = 0
            currentFalseThrow     = 0
        elif(line[2] == "Starting"):
            for i in range(4, len(line)):
                #remove any "," from the string
                line[i] = line[i].replace(",", "")
                currentItemList.append(line[i])
        elif(line[2] == "Operation:"):
            currentOperator1 = line[5]
            currentOperationSign = line[6]
            currentOperator2 = line[7]
        elif(line[2] == "Test:"):
            currentDivisionNumber = int(line[5])
        elif(line[5] == "true:"):
            currentTrueThrow = int(line[9])
        elif(line[5] == "false:"):
            currentFalseThrow = int(line[9])
        else:
            print("error line is " + str(line))
    monkeyList.append(Monkey(currentOperator1, currentOperator2, currentOperationSign, currentDivisionNumber, currentTrueThrow, currentFalseThrow, currentItemList))
    for i in range(0, 20):
        for monkey in monkeyList:
            #print("monkey " + str(monkey.operand1) + " " + str(monkey.operandSign) + " " + str(monkey.operand2) + " " + str(monkey.divisionNumber) + " " + str(monkey.trueThrow) + " " + str(monkey.falseThrow) + " " + str(monkey.items))
            monkey.operate(monkeyList)
    for monkey in monkeyList:
        print("monkey " + str(monkeyList.index(monkey)) + " has items" + str(monkey.items) + ".")

    monkeyBussinessList = []
    for monkey in monkeyList:
        monkeyBussinessList.append(monkey.monkeyBussiness)
    #sort from highest to lowest
    monkeyBussinessList.sort(reverse=True)
    print(monkeyBussinessList)
    monkeyBussiness = monkeyBussinessList[0]*monkeyBussinessList[1]
    print ("monkey bussiness is " + str(monkeyBussiness))
    pass
def December11P2(lines):
     # first build the monkey list
    monkeyList = []
    currentItemList = []
    currentOperationSign = ""
    currentOperator1 = ""
    currentOperator2 = ""
    currentDivisionNumber = 0
    currentTrueThrow = 0
    currentFalseThrow = 0

    for line in lines:

        line = line.split(" ")
        #aprint (line)
        if(len(line) == 1):
            monkeyList.append(Monkey(currentOperator1, currentOperator2, currentOperationSign, currentDivisionNumber, currentTrueThrow, currentFalseThrow, currentItemList))
        elif(line[0] == "Monkey"):
            currentItemList= []
            currentOperationSign = ""
            currentOperator1 = ""
            currentOperator2 = ""
            currentDivisionNumber  = 0
            currentTrueThrow      = 0
            currentFalseThrow     = 0
        elif(line[2] == "Starting"):
            for i in range(4, len(line)):
                #remove any "," from the string
                line[i] = line[i].replace(",", "")
                currentItemList.append(line[i])
        elif(line[2] == "Operation:"):
            currentOperator1 = line[5]
            currentOperationSign = line[6]
            currentOperator2 = line[7]
        elif(line[2] == "Test:"):
            currentDivisionNumber = int(line[5])
            global worryLevelMagicNumber
            worryLevelMagicNumber *= currentDivisionNumber
        elif(line[5] == "true:"):
            currentTrueThrow = int(line[9])
        elif(line[5] == "false:"):
            currentFalseThrow = int(line[9])
        else:
            print("error line is " + str(line))
    monkeyList.append(Monkey(currentOperator1, currentOperator2, currentOperationSign, currentDivisionNumber, currentTrueThrow, currentFalseThrow, currentItemList))
    for i in range(0, 10000):
        for monkey in monkeyList:
            #print("monkey " + str(monkey.operand1) + " " + str(monkey.operandSign) + " " + str(monkey.operand2) + " " + str(monkey.divisionNumber) + " " + str(monkey.trueThrow) + " " + str(monkey.falseThrow) + " " + str(monkey.items))
            monkey.operate(monkeyList)
        if(i%10 == 0):
            print("loop number "+ str(i))
            for monkey in monkeyList:
                 print("monkey " + str(monkeyList.index(monkey)) + " has items" + str(monkey.items) + ".")
            pass
    for monkey in monkeyList:
        print("monkey " + str(monkeyList.index(monkey)) + " has items" + str(monkey.items) + ".")

    monkeyBussinessList = []
    for monkey in monkeyList:
        monkeyBussinessList.append(monkey.monkeyBussiness)
    #sort from highest to lowest
    monkeyBussinessList.sort(reverse=True)
    print(monkeyBussinessList)
    monkeyBussiness = monkeyBussinessList[0]*monkeyBussinessList[1]
    print ("monkey bussiness is " + str(monkeyBussiness))
    pass



realData = True
if realData == True:
    input_file = open("December11Input", "r")
else:
    input_file = open("testInput", "r")
input_data = input_file.read()
input_file.close()
lines = input_data.splitlines()

#December11P1(lines)
December11P2(lines)



#method to calculate the number n in the fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# method to calculate the number n in the factorial sequence
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# method to find if a number n is prime
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
