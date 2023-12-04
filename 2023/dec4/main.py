
#file = open("../input/dec4", "r")
file = open("../input/dec4", "r")

# put all the contents of the file in a array of arrays of chars
games = []
for line in file:
    #trim the line breaks
    line = line [0:-1]
    # remove the content before the first :
    line = line.split(":")[1]

    #split the values sepparated by a |
    values = line.split("|")
    winning_values = values[0].split(" ")
    given_values = values[1].split(" ")
    #remove any value that is empty
    winning_values = list(filter(None, winning_values))
    given_values = list(filter(None, given_values))

    #split the values separated by " "

    games.append((winning_values, given_values))
score =0
#make a list the size of the games array with 1s
original_scratch_cards = [1]*len(games)
for i in range(0, len(games)):
    winners=0
    amount_of_cards = original_scratch_cards[i]
    for given_value in games[i][1]:
        if given_value in games[i][0]:
            winners+=1
    if winners >= 1:
        for j in range(1, winners+1):
            original_scratch_cards[i+j] += amount_of_cards

score = sum(original_scratch_cards)
# for game in games:
#     #for each given value check if it is in the winning values
#     winners=0
#     for given_value in game[1]:
#         if given_value in game[0]:
#             winners+=1
#     if winners >= 1:
#         #add 2 to the power of the number of winners
#         score += 2**(winners-1)
#         print(score)
print(score)
