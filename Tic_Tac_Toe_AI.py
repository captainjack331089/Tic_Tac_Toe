
#Create a board
import random

board = []
for i in range(10):
    board.append(str(i))

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isWinner(board,letter):
    return (
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter)
           )


def isBoardFull(board):
    for i in board:
        if i.isdigit():
            return False
    return True


def insertBoard(board, user, pos):
    board[pos] = user


def spaceIsFree(board, pos):
    return board[pos].isdigit()


def playerMove(board, user):
    run = True
    while run:
        move = input("Please select a position to place an 'X'(1-9): ")
        try:
            move = int(move)
            #check the move is in the range
            if move >= 1 and move <= 9:
                #check the move is not occupied:
                if spaceIsFree(board, move):
                    run = False
                    insertBoard(board, user, move)
                else:
                    print("The position is occupied, please reselect!")

            else:
                print("Please type the number with the range(1-9)!")
        except:
            print("Please type a number!")


def pcMove(board, user_symbol, pc_symbol):
    """
    1: winning move
    2: protect defeat move
    3: center move
    4: corner move
    5: take rest of the position(randomly)
    :return:
    """

    pm = [x for x,letter in enumerate(board) if letter.isdigit() and x != 0]
    move = 0

    #1, 2 Winner or block defeat
    for l in [pc_symbol, user_symbol]:
        for i in pm:
            boardCopy = board[:]
            boardCopy[i] = l
            if isWinner(boardCopy, l):
                move = i
                return move

    # 3 go to the center
    if 5 in pm:
        move = 5
        return move

    #4 go to any corner
    corners = []
    for i in pm:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        move = random.choice(corners)
        return move

    #5 take the rest
    rest = []
    for i in pm:
        if i in [2,4,6,8]:
            rest.append(i)
    if len(rest) > 0:
        move = random.choice(rest)
    return move



def main():
    print("Welcome to Tic Tac Toe!")
    playboard = board[:]
    printBoard(playboard)
    user_symbol = "X"
    pc_symbol = "O"
    while not isBoardFull(playboard):
        if not (isWinner(playboard, pc_symbol)):
            playerMove(playboard, user_symbol)
            printBoard(playboard)
        else:
            print("Sorry, PC won the game this time!")
            choice = input("Do you want to play again? (y/n)")
            again = ['y', 'yes']
            if choice.lower() in again:
                main()
            else:
                break
        if not (isWinner(playboard, user_symbol)):
            move = pcMove(playboard, user_symbol, pc_symbol)
            if move == 0:
                print("Tie game!")
                choice = input("Do you want to play again? (y/n)")
                again = ['y', 'yes']
                if choice.lower() in again:
                    main()
                else:
                    exit()
            else:
                insertBoard(playboard, pc_symbol, move)
                print("PC has move 'O' to position: ", move , ":")
                printBoard(playboard)
        else:
            print("Congratulations! You won the game")
            choice = input("Do you want to play again? (y/n)")
            again = ['y', 'yes']
            if choice.lower() in again:
                main()
            else:
                break
    if isBoardFull(playboard):
        print("Tie game!")
        choice = input("Do you want to play again? (y/n)")
        again = ['y', 'yes']
        if choice.lower() in again:
            main()
        else:
            exit()

if __name__ == '__main__':
    main()