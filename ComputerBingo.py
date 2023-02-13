# Cianee Sumowalt
# 15 November 2022
# Bingo Game

import random

def create_card(length, width):
    bingo_card = [[0 for col in range(width)] for row in range(length)] #Initializes the card that is later overwritten
    nums_list = []
    for row in range(length):
        for col in range(width):
            unique = 'NO'
            while unique == 'NO':
                if col == 0:
                    num = random.randint(1,15) # depending on the column the numbers are different.
                elif col == 1:
                    num = random.randint(16,30)
                elif col == 2:
                    num = random.randint(31,45)
                elif col == 3:
                    num = random.randint(46,60)
                elif col == 4:
                    num = random.randint(61,75)
                if num not in nums_list:
                    nums_list.append(num)
                    bingo_card[row][col] = num
                    unique = 'YES'
    bingo_card[2][2] = 0 #This is always 0 because this is the free space
    return bingo_card

bingo_card = create_card(5, 5) # The dimensions can be changed here

def format_card(C): # C (for card) is bingo_card, which is used as a parameter
    print("\tB         \tI         \tN            \tG       \tO")
    for j in range(len(C)):
        for i in range(len(C[j])): # The loop prints one of each of the lists in a row, then it goes to the next line.
            print (f"\t{C[j][i]}",end="\t")
        print () #Needed to keep the Bingo Card looking like a bingo card. There's a bug where the 2D list gets printed with the formatted card.
    return C

def play_bingo(C):
 win = False
 call_list = []
 while win == False:
     comp_no = random.randint(1,75)
     if comp_no not in call_list:
        for row in range(0,5):
            for col in range(0,5):
                if C[row][col] == comp_no: #Checks the rows and columns to see if equal, if it is equal and unique, the number is added to the call list
                    C[row][col] = 0
                    call_list.append (comp_no)
                    win = is_Bingo(C) #After every loop we check for a win, if it returns false we go through the loop again, if true then we show the final card and the game ends
 if win == True:
         print(f"Call list = {call_list}")  # prints numbers called
         print ("BINGO!")
         print(format_card(C)) #prints the final card


def is_Bingo(C):
    rows = len(C)
    cols = len(C[0])
    if C[0][0] == 0 and C[1][1] == 0 and C[2][2] == 0 and C[3][3] == 0 and C[4][4] == 0 or C[0][4] == 0 and C[1][3] == 0 and C[2][2] == 0 and C[3][1] == 0 and C[4][0] == 0:
        return True
    for r in range(rows):
        if sum(C[r]) == 0:
            return True
    for c in range(cols):
        if sum(C[c])== 0:
            return True
    return False

print ("This program simulates the creation of a BINGO card\n and the subsequent simulation of a one card, one player game of BINGO.")
print (f"Selection list = {bingo_card}")
print (f"Your card = {format_card(bingo_card)}")

win = play_bingo(bingo_card)

