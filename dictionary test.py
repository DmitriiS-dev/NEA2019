import random


rulesDictionary ={'0, 0': None, '1, 0': 'bN1', '2, 0': 'bB2', '3, 0': None, '4, 0': 'bK', '5, 0': None, '6, 0': 'bN2', '7, 0': 'bR2',
                  '0, 1': 'bP1', '1, 1': None, '2, 1': 'bP3', '3, 1': 'bP5', '4, 1': 'bP5', '5, 1': 'bP6', '6, 1': 'bP7', '7, 1': 'bP8',
                  '0, 2': 'bP2', '1, 2': 'wP', '2, 2': 'bQ', '3, 2': 'wP', '4, 2': 'bP4', '5, 2': None, '6, 2': None, '7, 2': 'wP',
                  '0, 3': None, '1, 3': None, '2, 3': None, '3, 3': None, '4, 3': None, '5, 3': None, '6, 3': None, '7, 3': None,
                  '0, 4': None, '1, 4': None, '2, 4': 'bR1', '3, 4': None, '4, 4': None, '5, 4': 'bB1', '6, 4': None, '7, 4': None,
                  '0, 5': None, '1, 5': None, '2, 5': None, '3, 5': None, '4, 5': None, '5, 5': None, '6, 5': None, '7, 5': None,
                  '0, 6': None, '1, 6': 'wP', '2, 6': None, '3, 6': 'wP', '4, 6': 'wP', '5, 6': 'wP', '6, 6': 'wP', '7, 6': None,
                  '0, 7': 'wR', '1, 7': 'wN', '2, 7': 'wB', '3, 7': 'wQ', '4, 7': 'wK', '5, 7': 'wB', '6, 7': 'wN', '7, 7': 'wR'}



class AiMoves():
    def __init__(self):
        for Ai_key, Ai_value in rulesDictionary.items():
            if Ai_value != None:
                if Ai_value[0:3] == 'bP1':
                    self.bP1Moves = [
#               stores key to move from
                        [Ai_key],
#               stores key to move to
                        []]
                elif Ai_value[0:3] == 'bP2':
                    self.bP2Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bP3':
                    self.bP3Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bP4':
                    self.bP4Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bP5':
                    self.bP5Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bP6':
                    self.bP6Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bP7':
                    self.bP7Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bP8':
                    self.bP8Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bR1':
                    self.bR1Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bR2':
                    self.bR2Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bN1':
                    self.bN1Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bN2':
                    self.bN2Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bB1':
                    self.bB1Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:3] == 'bB2':
                    self.bB2Moves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:2] == 'bQ':
                    self.bQMoves = [
                        [Ai_key],
                        []]
                elif Ai_value[0:2] == 'bK':
                    self.bKMoves = [
                        [Ai_key],
                        []]

#pawn move AI
    def pawnMoves(self):
        pawnMove = str(self.A_key[1:2])+', '+str(int(self.A_key[4:5])+1)
        if rulesDictionary.get(pawnMove) is None:
            return pawnMove
        else:
            return None
        
#pawn 2 square move AI       
    def pawnMoves2(self):
        pawnMove = str(self.A_key[1:2])+', '+str(self.A_key[4:5])
        temp1 = rulesDictionary.get(pawnMove[0:1]+', '+str(int(pawnMove[3:4])+1))
        temp2 = rulesDictionary.get(pawnMove[0:1]+', '+str(int(pawnMove[3:4])+2))
        if pawnMove[3:4] == '1':
            if temp1 is None and temp2 is None:
                return str(pawnMove[0:1])+', '+str(int(pawnMove[3:4])+2)
        else:
            return None
        
#pawn Capture AI
    def pawnCaptures(self):
        pawnMove = str(self.A_key[1:2])+', '+str(self.A_key[4:5])
        availableLeft = str(int(pawnMove[0:1])-1)+', '+str(int(pawnMove[3:4])+1)
        availableRight = str(int(pawnMove[0:1])+1)+', '+str(int(pawnMove[3:4])+1)
        getLeft = rulesDictionary.get(availableLeft)
        getRight = rulesDictionary.get(availableRight)
        if availableLeft[0:2] == '-1':
            if getRight is not None and getRight[0:1] == 'w':
                return availableRight
            else:
                return None
        elif availableRight[0:1] == '8':
            if getLeft is not None and getLeft[0:1] == 'w':
                return availableLeft
            else:
                return None
        elif getLeft is not None and getLeft[0:1] == 'w':
            if getRight is not None and getRight[0:1] == 'w':
                return [availableLeft, availableRight]
            else:
                return availableLeft
        elif getRight is not None and getRight[0:1] == 'w':
            if getLeft is not None and getLeft[0:1] == 'w':
                return [availableRight, availableLeft]
            else:
                return availableRight
        else:
            return None
#knight AI
    def KnightMoves(self):
        knightMove = self.A_key
        x = knightMove[0:1]
        y = knightMove[3:4]
        move1 = str(int(x)+2)+', '+str(int(y)-1)
        move2 = str(int(x)+2)+', '+str(int(y)+1)
        
        move3 = str(int(x)-2)+', '+str(int(y)-1)
        move4 = str(int(x)-2)+', '+str(int(y)+1)
        
        move5 = str(int(x)-1)+', '+str(int(y)-2)
        move6 = str(int(x)+1)+', '+str(int(y)-2)
        
        move7 = str(int(x)+1)+', '+str(int(y)+2)
        move8 = str(int(x)-1)+', '+str(int(y)+2)
        moveList = []
        moveList.append(move1)
        moveList.append(move2)
        moveList.append(move3)
        moveList.append(move4)
        moveList.append(move5)
        moveList.append(move6)
        moveList.append(move7)
        moveList.append(move8)
        #important why I did reversed: error python thinks it has allready looped through that index.
        for element in reversed(moveList):
            if element[0:1] == '-' or element[3:4] == '-' or element[4:5] == '-' or element[0:1] == '8' or element[0:1] == '9' or element[3:4] == '8' or element[3:4] == '9' or element[4:5] == '8' or element[4:5] == '9':
                moveList.remove(element)
        for element in reversed(moveList):
            element2 = rulesDictionary.get(element)
            if element2 is not None:
                if element2[0:1] == 'b':
                    moveList.remove(element)
                else:
                    pass
        return moveList
#Diagonal moves AI:
    def rightDown(self):
        move = self.A_key
        rightDown_List = []
        for i in range(1,7):
            x = int(move[0:1])+i
            y = int(move[3:4])+i
            element2 = rulesDictionary.get(str(x)+', '+str(y))
            move2 = str(x)+', '+str(y)
            if x > 7 or y > 7:
                return rightDown_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    rightDown_List.append(move2)
                    return rightDown_List
                else:
                    return rightDown_List
            rightDown_List.append(move2)
        return rightDown_List

    def leftUp(self):
        move = self.A_key
        leftUp_List = []
        for i in range(1,7):
            x = int(move[0:1])-i
            y = int(move[3:4])-i
            element2 = rulesDictionary.get(str(x)+', '+str(y))
            move2 = str(x)+', '+str(y)
            if x < 0 or y < 0:
                return leftUp_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    leftUp_List.append(move2)
                    return leftUp_List
                else:
                    return leftUp_List
            leftUp_List.append(move2)
        return leftUp_List

    def leftDown(self):
        move = self.A_key
        leftDown_List = []
        for i in range(1,7):
            x = int(move[0:1])-i
            y = int(move[3:4])+i
            element2 = rulesDictionary.get(str(x)+', '+str(y))
            move2 = str(x)+', '+str(y)
            if x < 0 or y > 7:
                return leftDown_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    leftDown_List.append(move2)
                    return leftDown_List
                else:
                    return leftDown_List
            leftDown_List.append(move2)
        return leftDown_List

    def rightUp(self):
        move = self.A_key
        rightUp_List = []
        for i in range(1,7):
            x = int(move[0:1])+i
            y = int(move[3:4])-i
            element2 = rulesDictionary.get(str(x)+', '+str(y))
            move2 = str(x)+', '+str(y)
            if x > 7 or y < 0:
                return rightUp_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    rightUp_List.append(move2)
                    return rightUp_List
                else:
                    return rightUp_List
            rightUp_List.append(move2)
        return rightUp_List

#Side to side, Up and Down moves AI:
    def Up(self):
        move = self.A_key
        Up_List = []
        for i in range(1,7):
            x = move[0:1]
            y = int(move[3:4])-i
            element2 = rulesDictionary.get(x+', '+str(y))
            move2 = x+', '+str(y)
            if y < 0:
                return Up_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    Up_List.append(move2)
                    return Up_List
                else:
                    return Up_List
            Up_List.append(move2)
        return Up_List

    def Down(self):
        move = self.A_key
        Down_List = []
        for i in range(1,7):
            x = move[0:1]
            y = int(move[3:4])+i
            element2 = rulesDictionary.get(x+', '+str(y))
            move2 = x+', '+str(y)
            if y > 7:
                return Down_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    Down_List.append(move2)
                    return Down_List
                else:
                    return Down_List
            Down_List.append(move2)
        return Down_List

    def sideLeft(self):
        move = self.A_key
        left_List = []
        for i in range(1,7):
            x = int(move[0:1])-i
            y = move[3:4]
            element2 = rulesDictionary.get(str(x)+', '+y)
            move2 = str(x)+', '+y
            if x < 0:
                return left_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    left_List.append(move2)
                    return left_List
                else:
                    return left_List
            left_List.append(move2)
        return left_List

    def sideRight(self):
        move = self.A_key
        right_List = []
        for i in range(1,7):
            x = int(move[0:1])+i
            y = move[3:4]
            element2 = rulesDictionary.get(str(x)+', '+y)
            move2 = str(x)+', '+y
            if x > 7:
                return right_List
            elif element2 is not None:
                if element2[0:1] == 'w':
                    right_List.append(move2)
                    return right_List
                else:
                    return right_List
            right_List.append(move2)
        return right_List   
    
#bishop AI:
    def BishopMoves(self):
        movesList = []
        right_Down = self.rightDown()
        right_Up = self.rightUp()
        left_Down = self.leftDown()
        left_Up = self.leftUp()
        for element in right_Down:
            movesList.append(element)
        for element in right_Up:
            movesList.append(element)
        for element in left_Down:
            movesList.append(element)
        for element in left_Up:
            movesList.append(element)
        return movesList
    
#rook AI:
    def RookMoves(self):
        movesList = []
        Up = self.Up()
        Down = self.Down()
        side_Left = self.sideLeft()
        side_Right = self.sideRight()
        for element in Up:
            movesList.append(element)
        for element in Down:
            movesList.append(element)
        for element in side_Left:
            movesList.append(element)
        for element in side_Right:
            movesList.append(element)
        return movesList

#Queen AI:
    def QueenMoves(self):
        movesList = []
        Up = self.Up()
        Down = self.Down()
        side_Left = self.sideLeft()
        side_Right = self.sideRight()
        right_Down = self.rightDown()
        right_Up = self.rightUp()
        left_Down = self.leftDown()
        left_Up = self.leftUp()
        for element in Up:
            movesList.append(element)
        for element in Down:
            movesList.append(element)
        for element in side_Left:
            movesList.append(element)
        for element in side_Right:
            movesList.append(element)
        for element in right_Down:
            movesList.append(element)
        for element in right_Up:
            movesList.append(element)
        for element in left_Down:
            movesList.append(element)
        for element in left_Up:
            movesList.append(element)
        return movesList
        
#King AI
    def KingMoves(self):
        moveList = []
        kingMove = self.A_key
        x = kingMove[0:1]
        y = kingMove[3:4]
        #up and down
        move1 = x+', '+str(int(y)-1)
        move2 = x+', '+str(int(y)+1)
        #move left and right
        move3 = str(int(x)+1)+', '+y
        move4 = str(int(x)-1)+', '+y
        #right then down and right then up
        move5 = str(int(x)+1)+', '+str(int(y)-1)
        move6 = str(int(x)+1)+', '+str(int(y)+1)
        #left then down and left then up
        move7 = str(int(x)-1)+', '+str(int(y)-1)
        move8 = str(int(x)-1)+', '+str(int(y)+1)
        moveList.append(move1)
        moveList.append(move2)
        moveList.append(move3)
        moveList.append(move4)
        moveList.append(move5)
        moveList.append(move6)
        moveList.append(move7)
        moveList.append(move8)
        for element in reversed(moveList):
            if element[0:1] == '-' or element[3:4] == '-' or element[4:5] == '-' or element[0:1] == '8' or element[0:1] == '9' or element[3:4] == '8' or element[3:4] == '9' or element[4:5] == '8' or element[4:5] == '9':
                moveList.remove(element)
        for element in reversed(moveList):
            element2 = rulesDictionary.get(element)
            if element2 is not None:
                if element2[0:1] == 'b':
                    moveList.remove(element)
                else:
                    pass
        return moveList
    
    def appending_bP1(self):
        A_key = self.bP1Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP1Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
# 2 pawn move AI:
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP1Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass
#pawn captures AI:
        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP1Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP1Moves)
            
#pawn number 2 AI        
    def appending_bP2(self):
        A_key = self.bP2Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP2Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
        
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP2Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass

        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP2Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP2Moves)
#pawn number 3 AI         
    def appending_bP3(self):
        A_key = self.bP3Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP3Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
        
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP3Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass

        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP3Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP3Moves)
        
#pawn number 4 AI        
    def appending_bP4(self):
        A_key = self.bP4Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP4Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
        
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP4Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass

        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP4Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP4Moves)

#pawn number 5 AI        
    def appending_bP5(self):
        A_key = self.bP5Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP5Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
        
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP5Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass

        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP5Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP5Moves)

#pawn number 6 AI       
    def appending_bP6(self):
        A_key = self.bP6Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP6Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
        
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP6Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass

        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP6Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP6Moves)

#pawn number 7 AI        
    def appending_bP7(self):
        A_key = self.bP7Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP7Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
        
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP7Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass

        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP7Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP7Moves)

#pawn number 8 AI        
    def appending_bP8(self):
        A_key = self.bP8Moves[0]
        self.A_key = str(A_key)[1:-1]
        reply = self.pawnMoves()
        if reply is not None:
            nestedList = self.bP8Moves[1]
            nestedList.append(reply)
        elif reply is None:
            pass
        
        reply2 = self.pawnMoves2()
        if reply2 is not None:
            nestedList = self.bP8Moves[1]
            nestedList.append(reply2)
        elif reply2 is None:
            pass

        reply3 = self.pawnCaptures()
        if reply3 is not None:
            nestedList = self.bP8Moves[1]
            if type(reply3) is list:
                nestedList.append(reply3[0])
                nestedList.append(reply3[1])
            else:
                nestedList.append(reply3)
        elif reply3 is None:
            pass
        print(self.bP8Moves)
        
#knight 1 AI
    def appending_bN1(self):
        A_key = self.bN1Moves[0]
        A_key = (str(A_key)[2:6])
        self.A_key = A_key
        reply = self.KnightMoves()
        nestedList = self.bN1Moves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bN1Moves)
        
#knight 2 AI
    def appending_bN2(self):
        A_key = self.bN2Moves[0]
        A_key = (str(A_key)[2:6])
        self.A_key = A_key
        reply = self.KnightMoves()
        nestedList = self.bN2Moves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bN2Moves)

#bishop 1 AI
    def appending_bB1(self):
        A_key = self.bB1Moves[0]
        self.A_key = (str(A_key)[2:6])
        reply = self.BishopMoves()
        nestedList = self.bB1Moves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bB1Moves)

#bishop 2 AI        
    def appending_bB2(self):
        A_key = self.bB2Moves[0]
        self.A_key = (str(A_key)[2:6])
        reply = self.BishopMoves()
        nestedList = self.bB2Moves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bB2Moves)

#rook 1 AI
    def appending_bR1(self):
        A_key = self.bR1Moves[0]
        self.A_key = (str(A_key)[2:6])
        reply = self.RookMoves()
        nestedList = self.bR1Moves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bR1Moves)
#rook 2  AI   
    def appending_bR2(self):
        A_key = self.bR2Moves[0]
        self.A_key = (str(A_key)[2:6])
        reply = self.RookMoves()
        nestedList = self.bR2Moves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bR2Moves)

#queen AI
    def appending_bQ(self):
        A_key = self.bQMoves[0]
        self.A_key = (str(A_key)[2:6])
        reply = self.QueenMoves()
        nestedList = self.bQMoves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bQMoves)

#king AI
    def appending_bK(self):
        A_key = self.bKMoves[0]
        self.A_key = (str(A_key)[2:6])
        reply = self.KingMoves()
        nestedList = self.bKMoves[1]
        for element in reply:
            nestedList.append(element)
        print(self.bKMoves)
        
# Should call the subroutine
    def order(self):
        self.appending_bP1()
        self.appending_bP2()
        self.appending_bP3()
        self.appending_bP4()
        self.appending_bP5()
        self.appending_bP6()
        self.appending_bP7()
        self.appending_bP8()
        self.appending_bN1()
        self.appending_bN2()
        self.appending_bB1()
        self.appending_bB2()
        self.appending_bR1()
        self.appending_bR2()
        self.appending_bQ()
        self.appending_bK()
        self.AiUpdates()

#Random move generator:   
    def randomMove(self):
        while True:
            piece = random.randint(1, 16)
            if piece == 1:
                length = (len(self.bP1Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP1Moves[0], self.bP1Moves[1][p]]
                else:
                    pass                
            elif piece == 2:
                length = (len(self.bP2Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP2Moves[0], self.bP2Moves[1][p]]
                else:
                    pass 
            elif piece == 3:
                length = (len(self.bP3Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP3Moves[0], self.bP3Moves[1][p]]
                else:
                    pass 
            elif piece == 4:
                length = (len(self.bP4Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP4Moves[0], self.bP4Moves[1][p]]
                else:
                    pass 
            elif piece == 5:
                length = (len(self.bP5Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP5Moves[0], self.bP5Moves[1][p]]
                else:
                    pass 
            elif piece == 6:
                length = (len(self.bP6Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP6Moves[0], self.bP6Moves[1][p]]
                else:
                    pass 
            elif piece == 7:
                length = (len(self.bP7Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP7Moves[0], self.bP7Moves[1][p]]
                else:
                    pass 
            elif piece == 8:
                length = (len(self.bP8Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bP8Moves[0], self.bP8Moves[1][p]]
                else:
                    pass 
            elif piece == 9:
                length = (len(self.bN1Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bN1Moves[0], self.bN1Moves[1][p]]
                else:
                    pass 
            elif piece == 10:
                length = (len(self.bN2Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bN2Moves[0], self.bN2Moves[1][p]]
                else:
                    pass 
            elif piece == 11:
                length = (len(self.bB1Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bB1Moves[0], self.bB1Moves[1][p]]
                else:
                    pass 
            elif piece == 12:
                length = (len(self.bB2Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bB2Moves[0], self.bB2Moves[1][p]]
                else:
                    pass
            elif piece == 13:
                length = (len(self.bR1Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bR1Moves[0], self.bR1Moves[1][p]]
                else:
                    pass
            elif piece == 14:
                length = (len(self.bR2Moves[1]))
                if length > 0:
                    p = random.randint(0, length-1)
                    return [self.bR2Moves[0], self.bR2Moves[1][p]]
                else:
                    pass
            elif piece == 15:
                length = (len(self.bKMoves[1]))
                if length > 0 :
                    p = random.randint(0, length-1)
                    return [self.bKMoves[0], self.bKMoves[1][p]]
                else:
                    pass
            elif piece == 16:
                length = (len(self.bQMoves[1]))
                if length > 0 :
                    p = random.randint(0, length-1)
                    return [self.bQMoves[0], self.bQMoves[1][p]]
                else:
                    pass

    def AiUpdates(self):
        move = self.randomMove()
        print(rulesDictionary.get(move[0][0]))
        print(rulesDictionary.get(move[1]))
#--------------------------------------------------------------------------------



      
call = AiMoves()
call.order()
    
        
#line_of_Sight = []
#This list comprehension would find the coords covered by the white pawns and output it:
#wP_covered_left = [str(int(key[0:1])-1) +', '+ str(int(key[3:4])-1) for key in rulesDictionary if rulesDictionary.get(key) == 'wP' and int(key[0:1]) > 0]
#wP_covered_right = [str(int(key[0:1])+1) +', '+ str(int(key[3:4])-1) for key in rulesDictionary if rulesDictionary.get(key) == 'wP' and int(key[0:1]) < 7]
#wP_covered_coords = wP_covered_left + wP_covered_right
#This list comprehension would find the coords covered by the black pawns and output it:
#bP_covered_left = [str(int(key[0:1])+1) +', '+ str(int(key[3:4])+1) for key in rulesDictionary if rulesDictionary.get(key) == 'bP' and int(key[0:1]) < 7]
#bP_covered_right = [str(int(key[0:1])-1) +', '+ str(int(key[3:4])+1) for key in rulesDictionary if rulesDictionary.get(key) == 'bP' and int(key[0:1]) > 0]
#bP_covered_coords = bP_covered_left + bP_covered_right
