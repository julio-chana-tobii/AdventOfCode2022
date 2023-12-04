print("hello world")

#open a file
# Path: 2023/dec3/main.py
file = open("../input/dec3", "r")
#file = open("../input/dec3", "r")

# put all the contents of the file in a array of arrays of chars
characters = []
for line in file:
    characters.append(list(line))
#create an struct called numbers that contains the number, the starting x and y and the ending x
numbers = []
for i in range(len(characters)):
    digitStarted = False
    for j in range(len(characters[i])):
        #if the character is a digit
        if characters[i][j].isdigit():
            if not digitStarted:
                #add the number to the array
                numbers.append([int(characters[i][j]), j, i, j])
                digitStarted = True
            else:
                #update the number
                numbers[len(numbers)-1][0] = numbers[len(numbers)-1][0]*10 + int(characters[i][j])
                #update the ending x
                numbers[len(numbers)-1][3] = j
        else:
            digitStarted = False
gears = []
for i in range(len(characters)):
    for j in range(len(characters[i])):
        if characters[i][j] == '*':
            gears.append([j, i])
#for each number and each gear, check if the gear touches the number
gears_connections = []
for i in range(len(gears)):
    for j in range(len(numbers)):
        if gears[i][0] >= numbers[j][1]-1 and gears[i][0] <= numbers[j][3]+1:
            if gears[i][1] >= numbers[j][2]-1 and gears[i][1] <= numbers[j][2]+1:
                gears_connections.append((i, numbers[j][0]))
#find all the gears that are connected to exactly 2 numbers
gears_connected_to_two_numbers = []
sum_gear_power = 0

for i in range(len(gears)):
    counter = 0
    product = 1
    for j in range(len(gears_connections)):
        if gears_connections[j][0] == i:
            counter += 1
            product *= gears_connections[j][1]
    if counter == 2:
        gears_connected_to_two_numbers.append(i)
        sum_gear_power += product
#find the product of the numbers
print(sum_gear_power)

# valid_numbers = []
# print(numbers)
# for i in range(len(numbers)):
#     #check all the characters around the number
#     characters_to_check = []
#     for j in range(numbers[i][1]-1, numbers[i][3]+2):
#         for k in range(numbers[i][2]-1, numbers[i][2]+2):
#             if k >= 0 and k < len(characters):
#                  if j >= 0 and j < len(characters[k]):
#                     characters_to_check.append(characters[k][j])
#     for j in range(len(characters_to_check)):
#         #check if the character is a digit
#         if not characters_to_check[j].isdigit():
#             #and character is not a . or linebreak
#             if characters_to_check[j] != '.' and characters_to_check[j] != '\n':
#                 #the number is valid
#                 valid_numbers.append(numbers[i][0])
#                 print(str(numbers[i][0]) + " is valid because " + str(characters_to_check[j]) + "is special " )
#                 break
# sum_valid_numbers = 0
# for i in range(len(valid_numbers)):
#     sum_valid_numbers += valid_numbers[i]
# print(sum_valid_numbers)
