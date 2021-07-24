class Board:
    
    class Mark:
        
        def __init__(self, X:int, Y:int, markIndex:int, symbol:str = 'D', id:str = None):
            self.__xCoordinate=X
            self.__yCoordinate=Y
            if (symbol=='') or (symbol==' '):
                symbol='D'
            self.__symbol=symbol
            self.__markIndex= markIndex
            self.__markID = id

        def setX(self, X:int):
            self.__xCoordinate = X

        def setY(self, Y:int):
            self.__yCoordinate = Y

        def setIndex(self, index:int):
            self.__markIndex = index

        def setSymbol(self, symbol:str = 'D'):
            self.__symbol = symbol

        def setID(self, id:str = None):
            self.__markID = id
        
        def getX(self):
            return self.__xCoordinate

        def getY(self):
            return self.__yCoordinate

        def getIndex(self):
            return self.__markIndex 

        def getSymbol(self):
            return self.__symbol

        def getID(self):
            if (self.__markID):
                return self.__markID
            else:
                return "None"      

    def __init__(self, nRows:int, nColumns:int):
        self.__rows = nRows
        self.__columns = nColumns
        self.__activeMarks=[]
        self.__numberOfMarks=len(self.__activeMarks)

    def __printError(self, errorCode:str):
        """Given an error code, this method raises an exception with a description of the error"""
        if errorCode == 'error01':
            raise ValueError('ERROR: Column number not valid. Max column coordinate is', self.__columns - 1)
        if errorCode == 'error02':
            raise ValueError('ERROR: Row number not valid. Max row coordinate is', self.__rows - 1)

    def __renewMarkIndex(self):
        """This method gives a new index number to each of the mark on the board, starting from number 1"""
        index=1
        for i in self.__activeMarks:
            i.setIndex(index)
            index+=1
        del index
    
    def __getMark(self, xCoordinate, yCoordinate):
        """Given the X coordinate [xCoordinate] and the Y coordinate, this method returns the object:Mark located in those coordinates inside the board. If no mark is found, the method returns False"""
        for i in self.__activeMarks:
            if (i.getX() == xCoordinate) and (i.getY() == yCoordinate):
                return i
        return False

    def printXYBoard(self):
        """Prints the current state of the board"""
        for y in range(self.__rows):
            for x in range(self.__columns):
                if isinstance(self.__getMark(x,y), Board.Mark):
                    print('['+str(self.__getMark(x,y).getSymbol())+']',end='')
                else:
                    print('[ ]',end='')
            print('')
    
    def addNewMark(self, xCoordinate:int, yCoordinate:int, symbol:str = '', markID:str = None):
        """Adds a new mark to an existing board, given the position in the X axis [xCoordinate], the position in the Y axis [yCoordinate], and the symbol the mark is going to have [symbol]"""
        if xCoordinate > self.__columns - 1:
            self.__printError('error01')
        elif yCoordinate > self.__rows - 1:
            self.__printError('error02')
        else:
            newMark = Board.Mark(xCoordinate, yCoordinate,self.__numberOfMarks+1, symbol, markID)
            self.__activeMarks.append(newMark)
            del newMark
            self.__numberOfMarks = self.__numberOfMarks + 1

    def removeMark(self, markIndex:int):
        """Given an index [markIndex], this method removes the mark that has that index, and renews the indexes of all remaining marks to mantain the order"""
        for i in self.__activeMarks:
            if i.getIndex() == markIndex:
                self.__activeMarks.remove(i)
        self.__numberOfMarks = self.__numberOfMarks - 1
        self.__renewMarkIndex()

    def showCurrentMarks(self):
        """This method prints a list with all existing marks inside a board, following this template:
        INDEX : [ X , Y ] | Symbol: SYMBOL | Id: ID"""
        for i in self.__activeMarks:
            print(i.getIndex() , ': [' , i.getX() , ',' , i.getY() , '] | Symbol: ', i.getSymbol(), '| ID: ', i.getID())

    def getNumberOfMarks(self):
        return self.__numberOfMarks
