# Tic_Tac_Toe
 A simple Tic Tac Toe python application

##### Step To create this app:

- Create a Board
    - board is consisted of number 1 - 9 
    - digit 1- 9 is for user to select use. 

- Create user/pc symbol "O" / "X" 
    - Can let user choose later if script enhanced.

- Create a winning rule:
    - any position vertical,horizonal,diagonally equal to either "O" or "X", win
    - else winning not happen.

- Create a isBoardFull function
    - if all positions on board is not digit("O" or "X"):
        full
    - if not full: 
        - Check if any winning happens:
            - if isWin happens: end the game and let user choose restart or not.
            - if isWin not happen: let user to choose the position to place
             the move.
             
- Create spaceIsFree function:
    - Check the position the user select is free(is a digit)
    - if free, can put the move
    - if not free, let the user reselect 
    
- Create playerMove function
    - let user choose the position on the board to move.
    - move should be in range(1-9) and is a digit
        - if not valid, let user reselect.
        - if space is not free, let user reselect.
    - move is valid, insert the move to the board
        - update the board and print the board to the prompt

- Create PCMove Function:
    
    1: winning move 
    
    2: protect defeat move
    
    - 1 + 2
        - create a stack to save all possible moves on the board
        - position should not be 0
        - position should be a digit on the board
        - try virtual move of "O" on the current copied board and to see if any move could make isWin happen.
            - if happen, return this move
        - try virtual move of "X" on the current copied board and to see if any move could make isWin Happen.
            - if happen, return this move      
    
    3: center move
    
    - center means 5:
        - if 5 exist, return 5
    
    4: corner move
    - corner move means: 1, 3, 4, 7
        - if any of them exists, append to a temp stack
        - random select the element from the temp stack and return it.
    
    5: take rest of the position(randomly)
    - rest move means: 2, 4, 6, 8
        - if any of them exists, append to a temp stack
        - random select the element from the temp stack and return it.

- Create a boradIsFull Function:
    - Check if board is full(no any digit)
    - if True, print: "game is tied." and ask user to exit or restart.    
    
   
         
      
             
    
