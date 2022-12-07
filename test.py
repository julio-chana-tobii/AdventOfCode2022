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
December7P2(True)
