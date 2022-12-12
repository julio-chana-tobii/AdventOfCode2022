#import common libraries
import os
import sys
import time
import math
import sys
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
headposition = [0,0]
tailposition = []
def moveHead(direction):
    if direction == "U":
        headposition[1] += 1
    elif direction == "D":
        headposition[1] -= 1
    elif direction == "L":
        headposition[0] -= 1
    elif direction == "R":
        headposition[0] += 1
    else:
        print("invalid direction")
def tailCatchup():
    delta_x = headposition[0] - tailposition[0]
    delta_y = headposition[1] - tailposition[1]
    if delta_x > 1:
        tailposition[0] += 1
        if(delta_y>0):
            tailposition[1] += 1
        elif(delta_y<0):
            tailposition[1] -= 1
    elif delta_x < -1:
        tailposition[0] -= 1
        if(delta_y>0):
            tailposition[1] += 1
        elif(delta_y<0):
            tailposition[1] -= 1
    elif delta_y > 1:
        tailposition[1] += 1
        if(delta_x>0):
            tailposition[0] += 1
        elif(delta_x<0):
            tailposition[0] -= 1
    elif delta_y < -1:
        tailposition[1] -= 1
        if(delta_x>0):
            tailposition[0] += 1
        elif(delta_x<0):
            tailposition[0] -= 1
    
    return tailposition[0], tailposition[1]
def tailCatchup9():
    for i in range(0, 9):
        if i==0:
            delta_x = headposition[0] - tailposition[i][0]
            delta_y = headposition[1] - tailposition[i][1]
        else:
            delta_x = tailposition[i-1][0] - tailposition[i][0]
            delta_y = tailposition[i-1][1] - tailposition[i][1]
        if delta_x > 1:
            tailposition[i][0] += 1
            if(delta_y>0):
                tailposition[i][1] += 1
            elif(delta_y<0):
                tailposition[i][1] -= 1
        elif delta_x < -1:
            tailposition[i][0] -= 1
            if(delta_y>0):
                tailposition[i][1] += 1
            elif(delta_y<0):
                tailposition[i][1] -= 1
        elif delta_y > 1:
            tailposition[i][1] += 1
            if(delta_x>0):
                tailposition[i][0] += 1
            elif(delta_x<0):
                tailposition[i][0] -= 1
        elif delta_y < -1:
            tailposition[i][1] -= 1
            if(delta_x>0):
                tailposition[i][0] += 1
            elif(delta_x<0):
                tailposition[i][0] -= 1
    return tailposition[8][0], tailposition[8][1]

    pass
def December9P1(real_data):
     #read input file
    if real_data == True:
        input_file = open("December9Input", "r")
    else:
        input_file = open("testInput", "r")
    input_data = input_file.read()
    input_file.close()
    #split input into lines
    input_data = input_data.splitlines()
    tailPositions = []
    for line in input_data:
        #split by spaces
        line = line.split(" ")
        
        direction = line[0]
        distance = int(line[1])
        for i in range(0, distance):
            moveHead(direction)
            print("h" + str(headposition))
            newTailPosition =tailCatchup()

            #if tail is in a new position
            print("t" + str(newTailPosition))
            if newTailPosition not in tailPositions:
                tailPositions.append(newTailPosition)

    print(len(tailPositions))
        
def December9P2(real_data):
    #read input file
    if real_data == True:
        input_file = open("December9Input", "r")
    else:
        input_file = open("testInput", "r")
    input_data = input_file.read()
    input_file.close()
    #split input into lines
    input_data = input_data.splitlines()
    tailPositions = []
    for i in range(0, 9):
        tailposition.append([0,0])
        print(tailposition[i])
    for line in input_data:
        #split by spaces
        line = line.split(" ")
        
        direction = line[0]
        distance = int(line[1])
        for i in range(0, distance):
            moveHead(direction)
            print("h" + str(headposition))
            newTailPosition =tailCatchup9()

            #if tail is in a new position
            print("t" + str(newTailPosition))
            if newTailPosition not in tailPositions:
                tailPositions.append(newTailPosition)
    print(len(tailPositions))
distanceMap =[]
#December9P2(True)
def updateNeighborsDisanceToStart(point, map):
    #check if point is in map
    global distanceMap
    if point[0] < 0 or point[0] >= len(map) or point[1] < 0 or point[1] >= len(map[0]):
        return
    #check neighbors
    currentDistance = distanceMap[point[0]][point[1]]
    newDistance = currentDistance + 1
    southPoint = [point[0]+1, point[1]]
    northPoint = [point[0]-1, point[1]]
    eastPoint = [point[0], point[1]+1]
    westPoint = [point[0], point[1]-1]
    pointsToCheck = [southPoint, northPoint, eastPoint, westPoint]

    for pointcheck in pointsToCheck:
        if pointcheck[0] < 0 or pointcheck[0] >= len(map) or pointcheck[1] < 0 or pointcheck[1] >= len(map[0]):
            continue
        deltaHeight = map[pointcheck[0]][pointcheck[1]] - map[point[0]][point[1]]
        if deltaHeight <= 1:
            if(newDistance < distanceMap[pointcheck[0]][pointcheck[1]]):
                distanceMap[pointcheck[0]][pointcheck[1]] = newDistance
                # print("updating " + str(pointcheck) + " of height "+ str(map[pointcheck[0]][pointcheck[1]])+" to " + str(newDistance))
                updateNeighborsDisanceToStart(pointcheck, map)

    
    
def December12P1(data):
    data = data.splitlines()
    heightArray= {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25, "S":0, "E":25}
    currentPoint = [0,0]
    targetPoint = [0,0]
    map = []
    for i in range(0, len(data)):
        map.append([])
        for j in range(0, len(data[i])):
            map[i].append(heightArray[data[i][j]])
            if(data[i][j] == "S"):
                currentPoint = [i,j]
            elif(data[i][j] == "E"):
                targetPoint = [i,j]
            elif(data[i][j] == "Z"):
                targetPoint =  [i,j]
    
    print (map)
    global distanceMap
    for i in range(0, len(data)):
        distanceMap.append([])
        for j in range(0, len(data[i])):
            distanceMap[i].append(10000)
    distanceMap[currentPoint[0]][currentPoint[1]] = 0
    print(currentPoint)
    print(distanceMap[currentPoint[0]][currentPoint[1]])
    updateNeighborsDisanceToStart(currentPoint, map)
    print(distanceMap)
    print(distanceMap[targetPoint[0]][targetPoint[1]])

        
    pass
def December12P2(data):
    pass
#read input file
real_data = True
if real_data == True:
    input_file = open("December12Input", "r")
else:
    input_file = open("testInput", "r")
input_data = input_file.read()
input_file.close()

December12P1(input_data)