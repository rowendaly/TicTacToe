'''
Rowen Daly
January 2022
P.5 TIC-TAC-TOE
'''
#import statements go next
import random

#show your global variable

#function definitions
 #define the move function (player inputs row and column; check to see it's an available move, display the board)
def verify_guess(g): 
  while not g.isdigit() or int(g) < 1 or int(g) > 3:
    if not g.isdigit():
      g = input("You did not enter an integer. guess again") 
    else: 
      g = input("Your guess has to be between 1 and 3. Try again.")
  g = int(g) #now we know we can turn it into an int
  return g

def display_board(board):
  print("-------------------")
  for row in [0,1,2]:
    print("| "+board[row][0]+"  |  "+board[row][1]+"  |  "+board[row][2]+"  |")
    print("-------------------")

def move(player, letter):
  '''
  Perameters: player and letter
  Returns: nothing, grid will be updated with the move
  '''
  global grid
  
  if p1turn:
    row = verify_guess(input(player1+ ", please choose a row number:"))
    col = verify_guess(input(player1+ ", please choose a column number:"))
    while grid[row-1][col-1] !=" ":
      print("This square is not empty, try again")  
      row = verify_guess(input(player1+ ", please choose a row number:"))
      col = int(input("Enter column number:"))
    grid[row-1][col-1] = letter
    display_board(grid)
  else:
    row = verify_guess(input(player2+ ", please choose a row number:"))
    col = verify_guess(input(player2+ ", please choose a column number:"))
    while grid[row-1][col-1] !=" ":
      print("This square is not empty, try again")  
      row = verify_guess(input(player2+ ", please choose a row number:"))
      col = int(input("Enter column number:"))
    grid[row-1][col-1] = letter
    display_board(grid)



#----------Main code starts here-----------

#Welcome user and ask if they want to play tic-tac-toe (response)
response = input("Welcome! would you like to play Tic-Tac-Toe?")
def check_for_win(player, letter):
  #check the 3 rows and 3 columns, then check diagonals
  '''
  Parameters: players name(string) and the letter(string) 
  Returns: boolean (True or False) True if they won
  '''
  global grid
  for row in [0,1,2]: 
    if grid[row][0] == grid[row][1] == grid[row][2] == letter:
      return True
  for col in [0,1,2]:    
    if grid[0][col] == grid[1][col] == grid[2][col] == letter:
      return True
  #check for diagonals
  if grid[0][0] == grid[1][1] == grid[2][2] == letter:
    print(letter)
    return True
  if grid[0][2] == grid[1][1] == grid[2][0] == letter:
    return True
  return False
while response.lower()[0] == "y" or response.lower() [0:2] == "ok":
  # Ask for player names
  player1 = input("Enter name of Player1: ")
  player2 = input("Enter name of Player2: ")

  # Initialize our grid to an empty list(grid)
  grid = []
  # Clear the grid
  for row in [1,2,3]:
    grid.append([" "," "," "])
  display_board(grid)

  #boolean (True or False) Tur if they Won
  #randomley choose a player to go first
  p1turn = random.choice([True,False])

  xwins = False
  owins = False
  #(emptySquares - an int)
  emptySquares = 9
  #A while loop that checks to make sure no one has one and there are still empty spaces on board
  while not xwins and not owins and emptySquares > 0:
    #if it's player ones turn then:
    if p1turn:
      print(player1, ", it's your turn.")
      move(player1, "X")
      xwins = check_for_win(player1, "X")
      p1turn = False
    else:
      print(player2, ", it's your turn.")
      move(player2, "O")
      owins = check_for_win(player2, "O")
      p1turn = True
    emptySquares -= 1  #JUST TO STOP GAME
  if xwins:
    print("Congradulations " + player1 +". You won!")
  elif owins:
    print("Congradulations " + player2 +". You won!")
  else:
    print("Its a cat's game.")
  response = input("Would you like to play again? ")
print ("OK, goodbye. See you later.")
