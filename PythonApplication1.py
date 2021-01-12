# 5x5 Battleship with 4 attempts 

#from random file in python library using randint to get random integers for battlesipe location
from random import randint

#define open list for game-board
board = []

#loop generates 5x5 list of list of "O"s using append
for x in range(0, 5):
  board.append(["O"] * 5)

#function removes [] for each list from the 5x5 list of list. This is done by printing an open space and joining them by each row (one row is index 1 of list)
def print_board(board):
  for row in board:
    print (" ".join(row))

#prints board to output for user to see
print_board(board)

#function gets a random integer between 0-4 for row location of battleship
def random_row(board):
  return randint(0, len(board) - 1)

#function gets a random integer between 0-4 for col location of battleship
def random_col(board):
  return randint(0, len(board[0]) - 1)

#row and col location of battleship
ship_row = random_row(board)
ship_col = random_col(board)

#shows location of battleship (for debugging)
#print ship_row
#print ship_col

#for loops keeps track of users turn. 4 turns given and exits if user wins. prints number of turns each attempt.
for turn in range(4):
  
  #variables request input from user to get a guess of   location.
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  
  #if statement checks if users guess is equal to generated location of battleship.
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")
    #if correct breaks out out loop, program ends.
    break
  else:
    #checks if users inputs are within 0-4 range
    if guess_row not in range(5) or \
       guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    #checks if user entered a previously entered guess
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    #block reassigns the users guess location from "O" to "X" in list of list - board if users misses.
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print_board(board)
    #statements checks if users is out of turns, if so ends.
    if turn == 3:
      print ("Game Over")
  print ("Turn", turn+1)
