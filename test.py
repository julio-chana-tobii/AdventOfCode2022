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
realData = True
if realData == True:
    input_file = open("December10Input", "r")
else:
    input_file = open("testInput", "r")
input_data = input_file.read()
input_file.close()
lines = input_data.splitlines()

#December10p1(lines)
December10p2(lines)
