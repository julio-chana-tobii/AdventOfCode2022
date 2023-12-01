#import common libraries
import os
import sys
import time
import math
import sys

distanceMap =[]
#December9P2(True)
def updateNeighborsDisanceToEnd(point, map):
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
    atLeastOnePointUpdated = False
    for pointcheck in pointsToCheck:
        if pointcheck[0] < 0 or pointcheck[0] >= len(map) or pointcheck[1] < 0 or pointcheck[1] >= len(map[0]):
            continue
        deltaHeight = map[point[0]][point[1]] - map[pointcheck[0]][pointcheck[1]]
        if deltaHeight <= 1:
            if(newDistance < distanceMap[pointcheck[0]][pointcheck[1]]):
                distanceMap[pointcheck[0]][pointcheck[1]] = newDistance
                atLeastOnePointUpdated= True
                # print("updating " + str(pointcheck) + " of height "+ str(map[pointcheck[0]][pointcheck[1]])+" to " + str(newDistance))
               # updateNeighborsDisanceToStart(pointcheck, map)
    return atLeastOnePointUpdated
def UpdateAllPoints(map):
    global distanceMap
    atleastOnePointUpdated = False
    for i in range(0, len(map)):
        for j in range (0, len(map[0])):
            if updateNeighborsDisanceToEnd([i,j], map):
                atleastOnePointUpdated = True
    return atleastOnePointUpdated



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

    global distanceMap
    for i in range(0, len(data)):
        distanceMap.append([])
        for j in range(0, len(data[i])):
            distanceMap[i].append(10000)
    distanceMap[currentPoint[0]][currentPoint[1]] = 0

    while UpdateAllPoints(map):
        pass
    print(distanceMap[targetPoint[0]][targetPoint[1]])

    pass
def December12P2(data):
    data = data.splitlines()
    heightArray= {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25, "S":0, "E":25}
    possibleStartingPoints = []
    targetPoint = [0,0]
    map = []
    for i in range(0, len(data)):
        map.append([])
        for j in range(0, len(data[i])):
            map[i].append(heightArray[data[i][j]])
            if(data[i][j] == "S"):
                possibleStartingPoints.append([i,j])
            elif(data[i][j] == "E"):
                targetPoint = [i,j]
            elif(data[i][j] == "a"):
                possibleStartingPoints.append ([i,j])


    global distanceMap

    #for currentPoint in possibleStartingPoints:
    distanceMap = []
    for i in range(0, len(data)):
        distanceMap.append([])
        for j in range(0, len(data[i])):
            distanceMap[i].append(10000)
    distanceMap[targetPoint[0]][targetPoint[1]] = 0

    while UpdateAllPoints(map):
        pass
    lowest = 10000
    for currentPoint in possibleStartingPoints:
       # print(distanceMap[currentPoint[0]][currentPoint[1]])
        if distanceMap[currentPoint[0]][currentPoint[1]] < lowest:
            lowest = distanceMap[currentPoint[0]][currentPoint[1]]
    print (lowest)

    pass
#read input file
real_data = True
if real_data == True:
    input_file = open("December12Input", "r")
else:
    input_file = open("testInput", "r")
input_data = input_file.read()
input_file.close()

December12P2(input_data)
lines = input_data.splitlines()

#December11P1(lines)
#December11P2(lines)



