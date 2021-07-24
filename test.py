#This code was made with the intent of testing the board.py module


from board import *


def run():
    
    rows=int(input('Insert the number of rows: '))
    columns=int(input('Insert the number of columns: '))
    mainBoard = Board(rows,columns)

    while True:
        print('')
        print('MENU')
        print('1. print entire board')
        print('2. add new mark')
        print('3. remove existing mark')
        print('4. Show list of current marks')
        print('5. exit')
        menu=int(input('What should I do?: '))
        if menu == 1:
            mainBoard.printXYBoard()
        if menu == 2:
            xCoordinate = int(input('Enter X: '))
            yCoordinate = int(input('Enter Y: '))
            symbol = input('Enter symbol (blank for Default): ')
            markId = input('Enter an ID for this mark (Leave blank for default "None"): ')
            mainBoard.addNewMark(xCoordinate,yCoordinate,symbol, markId)
        if menu == 3:
            mainBoard.showCurrentMarks()
            index=int(input('Enter mark Index: '))
            mainBoard.removeMark(index)
        if menu == 4:
            mainBoard.showCurrentMarks()
        if menu == 5:
            break
        print('')
    wait=input()


if __name__=="__main__":
    run()
