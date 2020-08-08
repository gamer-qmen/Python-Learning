# Tic Tac Toe #

#variables
index = 0
cell_index = 0
var1 = 1 == 1
x_win = 1 == 0
o_win = 1 == 0
wins = []
cell = [" "," "," "," "," "," "," "," "," ",]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
use_numbers = ["1", "2", "3"]
player_side = "X"
player_counter = 0
"""
#player input
player_first = input("Enter cells: ")

#spliting player input into individual char in cell list
index = 0
while index <= 8:
    cell[index:index + 1] = player_first[index]
    index += 1
"""
#clear underscores
for n, i in enumerate(cell):
    if i == "_":
        cell[n] = " "

#print first board
#print board
print("---------")
print("|", cell[0], cell[1], cell[2], "|")
print("|", cell[3], cell[4], cell[5], "|")
print("|", cell[6], cell[7], cell[8], "|")
print("---------")

#defin win amount and place 012 345 678 036 147 258 048 246
if cell[0] == cell[1] == cell[2]:
    wins.append("1")
    if cell[0] == "X":
        x_win = 1 == 1
    elif cell[0] == "O":
        o_win = 1 == 1
if cell[3] == cell[4] == cell[5]:
    wins.append("2")
    if cell[3] == "X":
        x_win = 1 == 1
    elif cell[3] == "O":
        o_win = 1 == 1
if cell[6] == cell[7] == cell[8]:
    wins.append("3")
    if cell[6] == "X":
        x_win = 1 == 1
    elif cell[6] == "O":
        o_win = 1 == 1
if cell[0] == cell[3] == cell[6]:
    wins.append("4")
    if cell[0] == "X":
        x_win = 1 == 1
    elif cell[0] == "O":
        o_win = 1 == 1
if cell[1] == cell[4] == cell[7]:
    wins.append("5")
    if cell[1] == "X":
        x_win = 1 == 1
    elif cell[1] == "O":
        o_win = 1 == 1
if cell[2] == cell[5] == cell[8]:
    wins.append("6")
    if cell[2] == "X":
        x_win = 1 == 1
    elif cell[2] == "O":
        o_win = 1 == 1
if cell[0] == cell[4] == cell[8]:
    wins.append("7")
    if cell[0] == "X":
        x_win = 1 == 1
    elif cell[0] == "O":
        o_win = 1 == 1
if cell[2] == cell[4] == cell[6]:
    wins.append("8")
    if cell[2] == "X":
        x_win = 1 == 1
    elif cell[2] == "O":
        o_win = 1 == 1

#start gameplay loop
while x_win is False and o_win is False:
    #ask for input again
    player = input("Enter the coordinates: ")

    #define if input is valid
    valid_input1 = player[0] in numbers
    valid_input2 = player[2] in numbers
    if valid_input1 is False or valid_input2 is False:
        print("You should enter numbers!")
        continue
    valid_input1 = player[0] in use_numbers
    valid_input2 = player[2] in use_numbers
    if valid_input1 is False or valid_input2 is False:
        print("Coordinates should be from 1 to 3!")
        continue

    #define where the cords go and if space is free
    if player == "1 1":
        empty = " " == cell[6]
        if empty is True:
            cell[6] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "1 2":
        empty = " " == cell[3]
        if empty is True:
            cell[3] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "1 3":
        empty = " " == cell[0]
        if empty is True:
            cell[0] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "2 1":
        empty = " " == cell[7]
        if empty is True:
            cell[7] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "2 2":
        empty = " " == cell[4]
        if empty is True:
            cell[4] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "2 3":
        empty = " " == cell[1]
        if empty is True:
            cell[1] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "3 1":
        empty = " " == cell[8]
        if empty is True:
            cell[8] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "3 2":
        empty = " " == cell[5]
        if empty is True:
            cell[5] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue
    elif player == "3 3":
        empty = " " == cell[2]
        if empty is True:
            cell[2] = player_side
        else:
            print("This cell is occupied! Choose another one!")
            continue

    #print board
    print("---------")
    print("|", cell[0], cell[1], cell[2], "|")
    print("|", cell[3], cell[4], cell[5], "|")
    print("|", cell[6], cell[7], cell[8], "|")
    print("---------")

    #break loop after one is places
    if empty is True:
        if player_counter == 0:
            player_side = "O"
            player_counter = 1
        elif player_counter == 1:
            player_side = "X"
            player_counter = 0

    #defin win amount and place 012 345 678 036 147 258 048 246
    if cell[0] == cell[1] == cell[2]:
        wins.append("1")
        if cell[0] == "X":
            x_win = 1 == 1
        elif cell[0] == "O":
            o_win = 1 == 1
    if cell[3] == cell[4] == cell[5]:
        wins.append("2")
        if cell[3] == "X":
            x_win = 1 == 1
        elif cell[3] == "O":
            o_win = 1 == 1
    if cell[6] == cell[7] == cell[8]:
        wins.append("3")
        if cell[6] == "X":
            x_win = 1 == 1
        elif cell[6] == "O":
            o_win = 1 == 1
    if cell[0] == cell[3] == cell[6]:
        wins.append("4")
        if cell[0] == "X":
            x_win = 1 == 1
        elif cell[0] == "O":
            o_win = 1 == 1
    if cell[1] == cell[4] == cell[7]:
        wins.append("5")
        if cell[1] == "X":
            x_win = 1 == 1
        elif cell[1] == "O":
            o_win = 1 == 1
    if cell[2] == cell[5] == cell[8]:
        wins.append("6")
        if cell[2] == "X":
            x_win = 1 == 1
        elif cell[2] == "O":
            o_win = 1 == 1
    if cell[0] == cell[4] == cell[8]:
        wins.append("7")
        if cell[0] == "X":
            x_win = 1 == 1
        elif cell[0] == "O":
            o_win = 1 == 1
    if cell[2] == cell[4] == cell[6]:
        wins.append("8")
        if cell[2] == "X":
            x_win = 1 == 1
        elif cell[2] == "O":
            o_win = 1 == 1

    if " " not in cell:
        break

#produce number of times both sides were played
x_plays = cell.count("X")# produces a true false if game is valid
o_plays = cell.count("O")
if x_plays > o_plays:
    game_condition = x_plays - o_plays
    var1 = game_condition == 1
elif o_plays > x_plays:
    game_condition = o_plays - x_plays
    var1 = game_condition == 1

#empty cell check
index = 0
while index <= 8:
    unfinished = "_" == cell[index]
    if unfinished is True:
        break
    index += 1

#test prints
"""
print(wins)
print(x_win)
print(o_win)
print(var1)
"""

#game output

if var1 is False:
    print("Impossible")
elif x_win is True and o_win is True:
    print("Impossible")
elif x_win is True:
    print("X wins")
elif o_win is True:
    print("O wins")
elif unfinished is True:
    print("Game not finished")
elif " " not in cell:
    print("Draw")

