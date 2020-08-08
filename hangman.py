# Write your code here
from typing import List, Any
print("H A N G M A N")
print('Type "play" to play the game, "exit"')
play = input("to quit: ")

if play == "exit":
    exit()

bank = ["python", "java", "kotlin", "javascript"]
import random

def findall(sub, string):
#    """
#    >>> text = "Allowed Hello Hollow"
#    >>> tuple(findall('ll', text))
#    (1, 10, 16)
#    """
    index = 0 - len(sub)
    try:
        while True:
            index = string.index(sub, index + len(sub))
            yield index
    except ValueError:
        pass

pick = random.choice(bank)
tries = 0
var1 = len(pick)
var2 = "-" * var1
index = 0
used = []
letter = ""
bet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
bet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while tries <=7:
    print("")
    if pick == var2:
        break
    elif pick == letter:
        var2 = letter
        break

    print(var2)
    letter = input("Input a letter: ")
    # win print
    if int(len(letter)) != 1:
        if tries ==7:
            print("You should input a single letter")
            print("No such letter in the word")
        else:
            print("You should input a single letter")
#            tries += 1
    elif letter in used:
        if tries ==7:
            print("You already typed this letter")
            print("No such letter in the word")
        else:
            print("You already typed this letter")
#            tries += 1
    elif letter not in bet:
        print("It is not an ASCII lowercase letter")
#        tries += 1
        if letter not in bet2:
            print("No such letter in the word")
    elif letter in pick:
        count = 1
        recount = 0
        index = list(findall(letter, pick))
        count = len(index)
        while count != 0:
#            print(index[recount:recount + 1])
            index3 = str(index[recount:recount + 1])
            index3 = index3[1:2]
            index2 = int(index3)
#            print(index2)
            var2 = var2[:index2] + letter + var2[index2 + 1:]
            count -= 1
            recount += 1
            used.append(letter)
    else:
        print("No such letter in the word")
        used.append(letter)
        tries += 1
        if tries >= 8:
            break


if pick == var2:
    print("")
    print(var2)
    print("You guessed the word!")
    print("You survived!")
else:
    print("You are hanged!")
