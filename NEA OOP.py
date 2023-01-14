#To the person reading this:
#   This will take quite some time to look through

import pygame
#pygame package is downloaded and imported
import random
#imbeded library package is retrieved to generate a random number
import time
#python library package 
#Initialise pygame
pygame.init()
#The board colours
white = (235,235,208)
green = (119,148,85)

#Dimensions for the board
dimension = 8
height = 400
width = 400
square = height // dimension

#sets dimensions for the window
screen = pygame.display.set_mode((width,height))

#Logo and Name for the game
pygame.display.set_caption("Chess Training App")
pygame.display.set_icon(pygame.image.load('images/chess-pieces.png'))


#Loads all the images into the following directories
wR = pygame.transform.scale(pygame.image.load("images/wR.png"), (square,square))
bR = pygame.transform.scale(pygame.image.load("images/bR.png"), (square,square))
wN = pygame.transform.scale(pygame.image.load("images/wN.png"), (square,square))
bN = pygame.transform.scale(pygame.image.load("images/bN.png"), (square,square))
wB = pygame.transform.scale(pygame.image.load("images/wB.png"), (square,square))
bB = pygame.transform.scale(pygame.image.load("images/bB.png"), (square,square))
wQ = pygame.transform.scale(pygame.image.load("images/wQ.png"), (square,square))
bQ = pygame.transform.scale(pygame.image.load("images/bQ.png"), (square,square))
wK = pygame.transform.scale(pygame.image.load("images/wK.png"), (square,square))
bK = pygame.transform.scale(pygame.image.load("images/bK.png"), (square,square))
wP = pygame.transform.scale(pygame.image.load("images/wP.png"), (square,square))
bP = pygame.transform.scale(pygame.image.load("images/bP.png"), (square,square))

#Dictionary for images
pieceValues = {'0, 0': bR, '1, 0': bN, '2, 0': bB, '3, 0': bQ, '4, 0': bK, '5, 0': bB, '6, 0': bN, '7, 0': bR,
                '0, 1': bP, '1, 1': bP, '2, 1': bP, '3, 1': bP, '4, 1': bP, '5, 1': bP, '6, 1': bP, '7, 1': bP,
                '0, 2': None, '1, 2': None, '2, 2': None, '3, 2': None, '4, 2': None, '5, 2': None, '6, 2': None, '7, 2': None,
                '0, 3': None, '1, 3': None, '2, 3': None, '3, 3': None, '4, 3': None, '5, 3': None, '6, 3': None, '7, 3': None,
                '0, 4': None, '1, 4': None, '2, 4': None, '3, 4': None, '4, 4': None, '5, 4': None, '6, 4': None, '7, 4': None,
                '0, 5': None, '1, 5': None, '2, 5': None, '3, 5': None, '4, 5': None, '5, 5': None, '6, 5': None, '7, 5': None,
                '0, 6': wP, '1, 6': wP, '2, 6': wP, '3, 6': wP, '4, 6': wP, '5, 6': wP, '6, 6': wP, '7, 6': wP,
                '0, 7': wR, '1, 7': wN, '2, 7': wB, '3, 7': wQ, '4, 7': wK, '5, 7': wB, '6, 7': wN, '7, 7': wR}

#Dictionary for pieces
rulesDictionary ={'0, 0': 'bR1', '1, 0': 'bN1', '2, 0': 'bB1', '3, 0': 'bQ', '4, 0': 'bK', '5, 0': 'bB2', '6, 0': 'bN2', '7, 0': 'bR2',
                  '0, 1': 'bP1', '1, 1': 'bP2', '2, 1': 'bP3', '3, 1': 'bP4', '4, 1': 'bP5', '5, 1': 'bP6', '6, 1': 'bP7', '7, 1': 'bP8',
                  '0, 2': None, '1, 2': None, '2, 2': None, '3, 2': None, '4, 2': None, '5, 2': None, '6, 2': None, '7, 2': None,
                  '0, 3': None, '1, 3': None, '2, 3': None, '3, 3': None, '4, 3': None, '5, 3': None, '6, 3': None, '7, 3': None,
                  '0, 4': None, '1, 4': None, '2, 4': None, '3, 4': None, '4, 4': None, '5, 4': None, '6, 4': None, '7, 4': None,
                  '0, 5': None, '1, 5': None, '2, 5': None, '3, 5': None, '4, 5': None, '5, 5': None, '6, 5': None, '7, 5': None,
                  '0, 6': 'wP1', '1, 6': 'wP2', '2, 6': 'wP3', '3, 6': 'wP4', '4, 6': 'wP5', '5, 6': 'wP6', '6, 6': 'wP7', '7, 6': 'wP8',
                  '0, 7': 'wR1', '1, 7': 'wN1', '2, 7': 'wB1', '3, 7': 'wQ', '4, 7': 'wK', '5, 7': 'wB2', '6, 7': 'wN2', '7, 7': 'wR2'}

#Draws the board
def drawBoard(screen):
    x = 0
    for i in range(8):
        pygame.draw.rect(screen, white, [x, 0, 50, 50])
        pygame.draw.rect(screen, green, [x, 50, 50, 50])
        pygame.draw.rect(screen, white, [x, 100, 50, 50])
        pygame.draw.rect(screen, green, [x, 150, 50, 50])
        pygame.draw.rect(screen, white, [x, 200, 50, 50])
        pygame.draw.rect(screen, green, [x, 250, 50, 50])
        pygame.draw.rect(screen, white, [x, 300, 50, 50])
        pygame.draw.rect(screen, green, [x, 350, 50, 50])
        x += 50
        pygame.draw.rect(screen, green, [x, 0, 50, 50])
        pygame.draw.rect(screen, white, [x, 50, 50, 50])
        pygame.draw.rect(screen, green, [x, 100, 50, 50])
        pygame.draw.rect(screen, white, [x, 150, 50, 50])
        pygame.draw.rect(screen, green, [x, 200, 50, 50])
        pygame.draw.rect(screen, white, [x, 250, 50, 50])
        pygame.draw.rect(screen, green, [x, 300, 50, 50])
        pygame.draw.rect(screen, white, [x, 350, 50, 50])
        x += 50  

#LIST-OF-AVAILABLE-CAPTURE-MOVES--------------------------------------------------------------
class availableMoves():
    def __init__(self):
        self.List = []

#Finds Moves that all white Pawns can capture             
    def pawnCapture(self, key):
        availableLeft = str(int(key[0:1])-1)+', '+str(int(key[3:4])-1)
        availableRight = str(int(key[0:1])+1)+', '+str(int(key[3:4])-1)
        getLeft = rulesDictionary.get(availableLeft)
        getRight = rulesDictionary.get(availableRight)
        if getLeft is not None and getLeft[0:1] == 'b' and getRight is not None and getRight[0:1] == 'b':
            self.List.append(availableLeft)
            self.List.append(availableRight)
        elif getLeft is not None and getLeft[0:1] == 'b' and getRight is None:
            self.List.append(availableLeft)
        elif getRight is not None and getRight[0:1] == 'b' and getLeft is None:
            self.List.append(availableRight)

#Finds Moves that all Knights can capture            
    def knightCapture(self, key):
        x = key[0:1]
        y = key[3:4]
        moveList = []
        moveList.append(str(int(x)+2)+', '+str(int(y)-1))
        moveList.append(str(int(x)+2)+', '+str(int(y)+1))
        moveList.append(str(int(x)-2)+', '+str(int(y)-1))
        moveList.append(str(int(x)-2)+', '+str(int(y)+1))
        moveList.append(str(int(x)-1)+', '+str(int(y)-2))
        moveList.append(str(int(x)+1)+', '+str(int(y)-2))
        moveList.append(str(int(x)+1)+', '+str(int(y)+2))
        moveList.append(str(int(x)-1)+', '+str(int(y)+2))
        for element in reversed(moveList):
            if rulesDictionary.get(element) is not None and rulesDictionary.get(element)[0:1] == 'b':
                self.List.append(element)
            else:
                pass
#DIAGONAL Capture:        
    def RD(self, key):
        for i in range(1,7):
            RD = str(int(key[0:1])+i)+', '+str(int(key[3:4])+i)
            if rulesDictionary.get(RD) is not None and rulesDictionary.get(RD)[0:1] == 'b':
                return RD
            elif rulesDictionary.get(RD) is not None and rulesDictionary.get(RD)[0:1] == 'w':
                return None
            
    def RU(self, key):
        for i in range(1,7):
            RU = str(int(key[0:1])+i)+', '+str(int(key[3:4])-i)
            if rulesDictionary.get(RU) is not None and rulesDictionary.get(RU)[0:1] == 'b':
                return RU
            elif rulesDictionary.get(RU) is not None and rulesDictionary.get(RU)[0:1] == 'w':
                return None
            
    def LD(self, key):
        for i in range(1,7):
            LD = str(int(key[0:1])-i)+', '+str(int(key[3:4])+i)
            if rulesDictionary.get(LD) is not None and rulesDictionary.get(LD)[0:1] == 'b':
                return LD
            elif rulesDictionary.get(LD) is not None and rulesDictionary.get(LD)[0:1] == 'w':
                return None
            
    def LU(self, key):
        for i in range(1,7):
            LU = str(int(key[0:1])-i)+', '+str(int(key[3:4])-i)
            if rulesDictionary.get(LU) is not None and rulesDictionary.get(LU)[0:1] == 'b':
                return LU
            elif rulesDictionary.get(LU) is not None and rulesDictionary.get(LU)[0:1] == 'w':
                return None
#--------------------------------
#LEFT, RIGHT, UP AND DOWN Capture:
    def U(self, key):
        for i in range(1,7):
            U = key[0:1]+', '+str(int(key[3:4])-i)
            if rulesDictionary.get(U) is not None and rulesDictionary.get(U)[0:1] == 'b':
                return U
            elif rulesDictionary.get(U) is not None and rulesDictionary.get(U)[0:1] == 'w':
                return None

    def D(self, key):
        for i in range(1,7):
            D = key[0:1]+', '+str(int(key[3:4])+i)
            if rulesDictionary.get(D) is not None and rulesDictionary.get(D)[0:1] == 'b':
                return D
            elif rulesDictionary.get(D) is not None and rulesDictionary.get(D)[0:1] == 'w':
                return None
    def R(self, key):
        for i in range(1,7):
            R = str(int(key[0:1])+i)+', '+key[3:4]
            if rulesDictionary.get(R) is not None and rulesDictionary.get(R)[0:1] == 'b':
                return R
            elif rulesDictionary.get(R) is not None and rulesDictionary.get(R)[0:1] == 'w':
                return None
    def L(self, key):
        for i in range(1,7):
            L = str(int(key[0:1])-i)+', '+key[3:4]
            if rulesDictionary.get(L) is not None and rulesDictionary.get(L)[0:1] == 'b':
                return L
            elif rulesDictionary.get(L) is not None and rulesDictionary.get(L)[0:1] == 'w':
                return None
#---------------------------------
#Finds Moves that all Bishops can capture
    def bishopCapture(self, key):
        RD1 = self.RD(key)
        RU1 = self.RU(key)
        LD1 = self.LD(key)
        LU1 = self.LU(key)
        if RD1 is not None:
            self.List.append(RD1)
        if RU1 is not None:
            self.List.append(RU1)
        if LD1 is not None:
            self.List.append(LD1)
        if LU1 is not None:
            self.List.append(LU1)
            
#Finds Moves that all Rooks can capture
    def rookCapture(self, key):
        U1 = self.U(key)
        D1 = self.D(key)
        R1 = self.R(key)
        L1 = self.L(key)
        if D1 is not None:
            self.List.append(D1)
        if U1 is not None:
            self.List.append(U1)
        if L1 is not None:
            self.List.append(L1)
        if R1 is not None:
            self.List.append(R1)
                    
#Finds Moves that Queen can capture
    def queenCapture(self, key):
        U1 = self.U(key)
        D1 = self.D(key)
        R1 = self.R(key)
        L1 = self.L(key)
        if D1 is not None:
            self.List.append(D1)
        if U1 is not None:
            self.List.append(U1)
        if L1 is not None:
            self.List.append(L1)
        if R1 is not None:
            self.List.append(R1)
        RD1 = self.RD(key)
        RU1 = self.RU(key)
        LD1 = self.LD(key)
        LU1 = self.LU(key)
        if RD1 is not None:
            self.List.append(RD1)
        if RU1 is not None:
            self.List.append(RU1)
        if LD1 is not None:
            self.List.append(LD1)
        if LU1 is not None:
            self.List.append(LU1)

    def kingCapture(self, key):
        moveList = []
        x = key[0:1]
        y = key[3:4]
        #up and down
        moveList.append(x+', '+str(int(y)-1))
        moveList.append(x+', '+str(int(y)+1))
        #move left and right
        moveList.append(str(int(x)+1)+', '+y)
        moveList.append(str(int(x)-1)+', '+y)
        #right then down and right then up
        moveList.append(str(int(x)+1)+', '+str(int(y)-1))
        moveList.append(str(int(x)+1)+', '+str(int(y)+1))
        #left then down and left then up
        moveList.append(str(int(x)-1)+', '+str(int(y)-1))
        moveList.append(str(int(x)-1)+', '+str(int(y)+1))
        for element in reversed(moveList):
            if rulesDictionary.get(element) is None:
                moveList.remove(element)
            elif rulesDictionary.get(element) is not None and rulesDictionary.get(element)[0:1] == 'w':
                moveList.remove(element)
        for element in moveList:
            self.List.append(element)
                
    def generatingValues(self):
        for key, value in rulesDictionary.items():
            #Pawn Moves:
            if value is not None and value[0:2] == 'wP':
                self.pawnCapture(key)
            #Knight Moves:
            elif value is not None and value[0:2] == 'wN':
                self.knightCapture(key)
            #Bishop Moves:
            elif value is not None and value[0:2] == 'wB':
                self.bishopCapture(key)
            elif value is not None and value[0:2] == 'wR':
                self.rookCapture(key)
            elif value is not None and value == 'wQ':
                self.queenCapture(key)
            elif value is not None and value == 'wK':
                self.kingCapture(key)

    def linearSearch(self):
        self.generatingValues()
        search_for = 'bK'
        search_at = 0
        response = False
        while search_at < len(self.List) and response is False:
            if rulesDictionary.get(self.List[search_at]) == search_for:
                response = True
            else:
                search_at = search_at +1
        return response
        
#LIST-OF-AVAILABLE-MOVES--------------------------------------------------------------


#CLASS-WHICH-CHECKS-IF-END-USER-HAS-MADE-A-VALID-MOVE--------------------------------               
class Rules():
#Initialise the class:
    def __init__(self):
        self.validMove = False
        self.from_Key = str(selected[0][0]) + ',' + ' ' + str(selected[0][1])
        self.to_Key = str(selected[1][0]) + ',' + ' ' + str(selected[1][1])
        self.Move2 = rulesDictionary.get(self.from_Key)
        self.Take2 = rulesDictionary.get(self.to_Key)

#   static method to which renders the font and returns it
    @staticmethod
    def windowLayout(message, font):
        colours = 'red', 'blue', 'chocolate1', 'darkslateblue',
        colour = random.choice(colours)
        surface = font.render(message, True, colour)
        return surface, surface.get_rect()
        
#   static method stores pop up window codes.
    @staticmethod
    def pop_up_windows(message):
        font_obj = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextCirc = Rules.windowLayout(message, font_obj)
        TextCirc.center = ((height/2), (width/2))
        screen.blit(TextSurf, TextCirc)
        pygame.display.update()
        time.sleep(2)
        

#   static method stores who's move it is so AI's or user's
    @staticmethod
    def getStatus(status):
        if status == 'Ai':  
            call = AiMoves()
            call.order()
        elif status == 'user':
            print('Success')

#Outer method to call the move validator methods              
    def Move(self):

        #inner method which is used to upgrade the user's pawn piece
        def upgrade(self):
#            screen.blit(wN, pygame.Rect(50, 50, 100, 100))
#            screen.blit(wB, pygame.Rect(100, 50, 100, 100))
#            screen.blit(wR, pygame.Rect(150, 50, 100, 100))
#            screen.blit(wQ, pygame.Rect(200, 50, 100, 100))
#            pygame.display.update()
    #finish of
            print("Enter 1 to convert your pawn to Knight")
            print('Enter 2 to convert your pawn to Bishop')
            print('Enter 3 to convert your pawn to Rook')
            print("Enter 4 to convert your pawn to Queen")
            upgrade = int(input("Choice: "))
            if upgrade == 1:
                pieceValues.update({self.from_Key : None})
                rulesDictionary.update({self.from_Key : None})
                pieceValues.update({self.to_Key : wN})
                rulesDictionary.update({self.to_Key : 'wN'})
            elif upgrade == 2:
                pieceValues.update({self.from_Key : None})
                rulesDictionary.update({self.from_Key : None})
                pieceValues.update({self.to_Key : wB})
                rulesDictionary.update({self.to_Key : 'wB'})
            elif upgrade == 3:
                pieceValues.update({self.from_Key : None})
                rulesDictionary.update({self.from_Key : None})
                pieceValues.update({self.to_Key : wR})
                rulesDictionary.update({self.to_Key : 'wR'})
            elif upgrade == 4:
                pieceValues.update({self.from_Key : None})
                rulesDictionary.update({self.from_Key : None})
                pieceValues.update({self.to_Key : wQ})
                rulesDictionary.update({self.to_Key : 'wQ'})
            else:
                print('Invalid input!')
#RULE 1:
        def attemptMoveAsBlack(self):
#       Here will be code for a pop up window
            self.validMove = False
            self.pop_up_windows('You cannot Move the Black pieces!')
            return self.validMove
        
#Inner method which prevents user selecting an empty square and it being a valid move
        def moveAsNothing(self):
            self.validMove = False
            self.pop_up_windows('Invalid Move!')
            return self.validMove
#RULE 2:          
        def attemptTakeWhitePiece(self):
            self.validMove = False
            self.pop_up_windows("You can not capture White pieces!")
            return self.validMove
        def pawn(self):
#RULE 3: Rule which would allow the user to move 2 pieces forward for the first pawn move
            if str(self.from_Key[3:4]) == '6' and str(self.to_Key[3:4]) == '4' and self.Take2 is None and str(self.from_Key[0:1]) == str(self.to_Key[0:1]):
                self.validMove = True
#RULE 4: Valid pawn move
            elif str(int(self.from_Key[3:4])-1) == str(self.to_Key[3:4]) and str(self.from_Key[0:1]) == str(self.to_Key[0:1]) and self.Take2 is None:
                self.validMove = True
#RULE 4: Valid pawn capture
            elif self.Take2 is not None and self.Take2[0:1] == 'b':
                if str(int(self.from_Key[0:1])-1) == str(self.to_Key[0:1]) and str(int(self.from_Key[3:4])-1) == str(self.to_Key[3:4]):
                    self.validMove = True
                elif str(int(self.from_Key[0:1])+1) == str(self.to_Key[0:1]) and str(int(self.from_Key[3:4])-1) == str(self.to_Key[3:4]):
                    self.validMove = True
            return self.validMove
#RULE 5: Valid move for Knight
        def knight(self):
            if self.Take2 is None or self.Take2[0:1] == 'b':
                if str(int(self.from_Key[0:1])+2) == str(self.to_Key[0:1]):
                    if str(int(self.from_Key[3:4])+1) == str(self.to_Key[3:4]):
                        self.validMove = True
                    elif str(int(self.from_Key[3:4])-1) == str(self.to_Key[3:4]):
                        self.validMove = True
                    else:
                        self.validMove = False
                elif str(int(self.from_Key[0:1])-2) == str(self.to_Key[0:1]):
                    if str(int(self.from_Key[3:4])+1) == str(self.to_Key[3:4]):
                        self.validMove = True
                    elif str(int(self.from_Key[3:4])-1) == str(self.to_Key[3:4]):
                        self.validMove = True
                    else:
                        self.validMove = False
                elif str(int(self.from_Key[3:4])+2) == str(self.to_Key[3:4]):
                    if str(int(self.from_Key[0:1])+1) == str(self.to_Key[0:1]):
                        self.validMove = True
                    elif str(int(self.from_Key[0:1])-1) == str(self.to_Key[0:1]):
                        self.validMove = True
                    else:
                        self.validMove = False
                elif str(int(self.from_Key[3:4])-2) == str(self.to_Key[3:4]):
                    if str(int(self.from_Key[0:1])+1) == str(self.to_Key[0:1]):
                        self.validMove = True
                    elif str(int(self.from_Key[0:1])-1) == str(self.to_Key[0:1]):
                        self.validMove = True
                    else:
                        self.validMove = False
                else:
                    self.validMove = False
            return self.validMove

#RULE 6: Valid move for Bishop        
        def bishop(self):
            if self.Take2 is None or self.Take2[0:1] == 'b':
#       Bishop moving diagonally left:
                if str(int(self.from_Key[3:4]) + int(self.from_Key[0:1])) == str(int(self.to_Key[3:4]) + int(self.to_Key[0:1])):
                    diagonally(self)
#       Bishop moving diagonally right:
                elif str((int(self.from_Key[3:4]) - int(self.to_Key[3:4]))*2) == str(int(self.from_Key[0:1]) - int(self.to_Key[0:1]) + int(self.from_Key[3:4])  - int(self.to_Key[3:4])):
                    diagonally(self)
                elif str((int(self.to_Key[3:4]) - int(self.from_Key[3:4]))*2) == str(int(self.to_Key[0:1]) - int(self.from_Key[0:1]) + int(self.to_Key[3:4])  - int(self.from_Key[3:4])):
                    diagonally(self)
                else:
                    self.validMove = False
            else:
                self.validMove = False
                return self.validMove
            return self.validMove
                    
#RULE 7: Valid move for Rook
        def rook(self):
            if self.Take2 is None or self.Take2[0:1] == 'b':
                if self.from_Key[0:1] == self.to_Key[0:1]:
                    up_down(self)
                elif self.from_Key[3:4] == self.to_Key[3:4]:
                    left_right(self)
                else:
                    self.validMove = False
                return self.validMove
                    
#RULE 8: Valid move for Queen
        def queen(self):
            if self.Take2 is None or self.Take2[0:1] == 'b':
#       Moving up, down, left and right
                if self.from_Key[0:1] == self.to_Key[0:1]:
                    up_down(self)
                elif self.from_Key[3:4] == self.to_Key[3:4]:
                    left_right(self)
#       Moving Diagonally Right up and Diagonally left down
                elif str(int(self.from_Key[3:4]) + int(self.from_Key[0:1])) == str(int(self.to_Key[3:4]) + int(self.to_Key[0:1])):
                    diagonally(self)
#       Moving Diagonally left and up
                elif str((int(self.from_Key[3:4]) - int(self.to_Key[3:4]))*2) == str(int(self.from_Key[0:1]) - int(self.to_Key[0:1]) + int(self.from_Key[3:4])  - int(self.to_Key[3:4])):
                    diagonally(self)
#       Moving Diagonally right and down                    
                elif str((int(self.to_Key[3:4]) - int(self.from_Key[3:4]))*2) == str(int(self.to_Key[0:1]) - int(self.from_Key[0:1]) + int(self.to_Key[3:4])  - int(self.from_Key[3:4])):
                    diagonally(self)
                else:
                    self.validMove = False
            return self.validMove

        def king(self):
            if self.Take2 is None or self.Take2[0:1] == 'b':
#       King moving to the right:
                if int(self.from_Key[0:1])+1 == int(self.to_Key[0:1]):
                    if int(self.from_Key[3:4])+1 == int(self.to_Key[3:4]):
                        self.validMove = True
                    elif int(self.from_Key[3:4]) == int(self.to_Key[3:4]):
                        self.validMove = True
                    elif int(self.from_Key[3:4]) -1 == int(self.to_Key[3:4]):
                        self.validMove = True
#       King moving the the left:
                elif int(self.from_Key[0:1]) -1 == int(self.to_Key[0:1]):
                    if int(self.from_Key[3:4]) +1 == int(self.to_Key[3:4]):
                        self.validMove = True
                    elif int(self.from_Key[3:4]) == int(self.to_Key[3:4]):
                        self.validMove = True
                    elif int(self.from_Key[3:4]) -1 == int(self.to_Key[3:4]):
                        self.validMove = True
#       King moving up and down:
                elif int(self.from_Key[0:1]) == int(self.to_Key[0:1]):
                    if int(self.from_Key[3:4]) +1 == int(self.to_Key[3:4]):
                        self.validMove = True
                    elif int(self.from_Key[3:4]) -1 == int(self.to_Key[3:4]):
                        self.validMove = True
#RULE 10: Castling
                elif self.to_Key == '2, 7' and self.from_Key == '4, 7':
                    if rulesDictionary.get('1, 7') is None and rulesDictionary.get('3, 7') is None and rulesDictionary.get('0, 7') == 'wR1'and rulesDictionary.get('2, 7') is None:
                        self.validMove = True
                        pieceValues.update({'0, 7' : None})
                        rulesDictionary.update({'0, 7' : None})
                        rulesDictionary.update({'3, 7' : 'wR1'})
                        pieceValues.update({'3, 7' : wR})
                elif self.to_Key == '6, 7' and self.from_Key == '4, 7':
                    if rulesDictionary.get('6, 7') is None and rulesDictionary.get('5, 7') is None and rulesDictionary.get('7, 7') == 'wR2':
                        self.validMove = True
                        pieceValues.update({'7, 7' : None})
                        rulesDictionary.update({'7, 7' : None})
                        rulesDictionary.update({'5, 7' : 'wR2'})
                        pieceValues.update({'5, 7' : wR})
                else:
                    self.validMove = False
                    
            return self.validMove

        def up_down(self):
            count = int(self.from_Key[3:4])
#               Down:
            if count < int(self.to_Key[3:4]):
                while count != int(self.to_Key[3:4]):
                    count += 1
                    if rulesDictionary.get(self.from_Key[0:1]+', '+str(count)) != None:
                        self.validMove = False
                        break
#               Up:                    
            elif count > int(self.to_Key[3:4]):
                while count != int(self.to_Key[3:4]):
                    count -= 1
                    if rulesDictionary.get(self.from_Key[0:1]+', '+str(count)) != None:
                        self.validMove = False
                        break
                        
            if self.from_Key[0:1]+', '+str(count) == self.to_Key:
                self.validMove = True
                
            return self.validMove

        def left_right(self):
            count = int(self.from_Key[0:1])
#           right
            if count < int(self.to_Key[0:1]):
                while count != int(self.to_Key[0:1]):
                    count +=1
                    if rulesDictionary.get(str(count)+', '+self.from_Key[3:4]) != None:
                        self.validMove = False
                        break
#           left
            elif count > int(self.to_Key[0:1]):
                while count != int(self.to_Key[0:1]):
                    count -=1
                    if rulesDictionary.get(str(count)+', '+self.from_Key[3:4]) != None:
                        self.validMove = False
                        break
            if str(count)+', '+self.from_Key[3:4] == self.to_Key:
                self.validMove = True
                
            return self.validMove

        def diagonally(self):
            count = int(self.from_Key[0:1])
            count2 = int(self.from_Key[3:4])
            while count != int(self.to_Key[0:1]):
#           count changes to move right_up:
                if count < int(self.to_Key[0:1]) and count2 > int(self.to_Key[3:4]):
                    count +=1
                    count2 -=1
                    if rulesDictionary.get(str(count)+', '+str(count2)) is not None and count != int(self.to_Key[0:1]):
                        self.validMove = False
                        return self.validMove
#           count changes to move left_down:
                elif count > int(self.to_Key[0:1]) and count2 < int(self.to_Key[3:4]):
                    count -=1
                    count2 +=1
                    if rulesDictionary.get(str(count)+', '+str(count2)) is not None and count != int(self.to_Key[0:1]):
                        self.validMove = False
                        return self.validMove
#           count changes to move left_up:
                elif count > int(self.to_Key[0:1]) and count2 > int(self.to_Key[3:4]):
                    count -=1
                    count2 -=1
                    if rulesDictionary.get(str(count)+', '+str(count2)) is not None and count != int(self.to_Key[0:1]):
                        self.validMove = False
                        return self.validMove
#           count changes to move right_down
                elif count < int(self.to_Key[0:1]) and count2 < int(self.to_Key[3:4]):
                    count +=1
                    count2 +=1
                    if rulesDictionary.get(str(count)+', '+str(count2)) is not None and count != int(self.to_Key[0:1]):
                        self.validMove = False
                        return self.validMove
                if count == int(self.to_Key[0:1]) and count2 == int(self.to_Key[3:4]):
                    self.validMove = True
                    return self.validMove

#UPDATING pieces:
        def pieceUpdate(self):
            self.Move = pieceValues.get(self.from_Key)
#Updates value in the main and second dictionary to None 
            pieceValues.update({self.from_Key : None})
            rulesDictionary.update({self.from_Key : None})
#Updates value in the main and second dictionary to Move to
            pieceValues.update({self.to_Key : self.Move})
            rulesDictionary.update({self.to_Key : self.Move2})

    #RULE 11: Change pawn to...
            for i in range(0,8):
                x_coord = str(i)
                upgrade1 = rulesDictionary.get(x_coord+', 0')
                if upgrade1 is not None and upgrade1[0:2] == 'wP':
                    upgrade(self)
                else:
                    pass            
                
    #Move as Nothing
        if self.Move2 is None:
            moveAsNothing(self)

    #RULE 1:Prevents user moving Black pieces
        elif self.Move2[0:1] == 'b':
            attemptMoveAsBlack(self)

    #RULE 2: Prevents user taking their own pieces (white)
        elif self.Take2 is not None and self.Take2[0:1] == 'w':
            attemptTakeWhitePiece(self)

    #Pawn:
        elif self.Move2[0:2] == 'wP':
            pawn(self)

    #RULE 5: Valid move for Knight
        elif self.Move2[0:2] == 'wN':
            knight(self)
                        
    #RULE 6: Valid move for Bishop
        elif self.Move2[0:2] == 'wB':
            bishop(self)

    #RULE 7: Valid move for Rook
        elif self.Move2[0:2] == 'wR':
            rook(self)
                        
    #RULE 8: Valid move for Queen
        elif self.Move2[0:2] == 'wQ':
            queen(self)

    #RULE 9: Valid move for King
        elif self.Move2[0:2] == 'wK':
            king(self)
                        
        if self.validMove == True:
            pieceUpdate(self)
            Rules.getStatus('Ai')

#CLASS-WHICH-CHECKS-IF-END-USER-HAS-MADE-A-VALID-MOVE--------------------------------

            
###---------------Code below is for the AI to generate all of the available moves:     
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
        moveList.append(x+', '+str(int(y)-1))
        moveList.append(x+', '+str(int(y)+1))
        #move left and right
        moveList.append(str(int(x)+1)+', '+y)
        moveList.append(str(int(x)-1)+', '+y)
        #right then down and right then up
        moveList.append(str(int(x)+1)+', '+str(int(y)-1))
        moveList.append(str(int(x)+1)+', '+str(int(y)+1))
        #left then down and left then up
        moveList.append(str(int(x)-1)+', '+str(int(y)-1))
        moveList.append(str(int(x)-1)+', '+str(int(y)+1))
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
#Castling:
        if rulesDictionary.get('5, 0') is None and rulesDictionary.get('6, 0') is None and rulesDictionary.get('4, 0') == 'bK' and rulesDictionary.get('7, 0') == 'bR2':
            moveList.append('6, 0')
        elif rulesDictionary.get('1, 0') is None and rulesDictionary.get('2, 0') is None and rulesDictionary.get('3, 0') is None and rulesDictionary.get('4, 0') == 'bK' and rulesDictionary.get('0, 0') == 'bR1':
            moveList.append('2, 0')
        return moveList
    
    def appending_bP1(self):
        try:         
            A_key = self.bP1Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP1Moves[1]
                nestedList.append(reply)
        # 2 pawn move AI:
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP1Moves[1]
                nestedList.append(reply2)
        #pawn captures AI:
            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP1Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass
            
#pawn number 2 AI        
    def appending_bP2(self):
        try:
            A_key = self.bP2Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP2Moves[1]
                nestedList.append(reply)
            
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP2Moves[1]
                nestedList.append(reply2)

            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP2Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass
#pawn number 3 AI         
    def appending_bP3(self):
        try:
            A_key = self.bP3Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP3Moves[1]
                nestedList.append(reply)
            
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP3Moves[1]
                nestedList.append(reply2)

            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP3Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass
        
#pawn number 4 AI        
    def appending_bP4(self):
        try: 
            A_key = self.bP4Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP4Moves[1]
                nestedList.append(reply)
            
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP4Moves[1]
                nestedList.append(reply2)

            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP4Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass

#pawn number 5 AI        
    def appending_bP5(self):
        try:  
            A_key = self.bP5Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP5Moves[1]
                nestedList.append(reply)
            
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP5Moves[1]
                nestedList.append(reply2)

            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP5Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass

#pawn number 6 AI       
    def appending_bP6(self):
        try:    
            A_key = self.bP6Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP6Moves[1]
                nestedList.append(reply)
            
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP6Moves[1]
                nestedList.append(reply2)

            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP6Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass

#pawn number 7 AI        
    def appending_bP7(self):
        try:           
            A_key = self.bP7Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP7Moves[1]
                nestedList.append(reply)
            
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP7Moves[1]
                nestedList.append(reply2)

            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP7Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass

#pawn number 8 AI        
    def appending_bP8(self):
        try:
            A_key = self.bP8Moves[0]
            self.A_key = str(A_key)[1:-1]
            reply = self.pawnMoves()
            if reply is not None:
                nestedList = self.bP8Moves[1]
                nestedList.append(reply)
            
            reply2 = self.pawnMoves2()
            if reply2 is not None:
                nestedList = self.bP8Moves[1]
                nestedList.append(reply2)

            reply3 = self.pawnCaptures()
            if reply3 is not None:
                nestedList = self.bP8Moves[1]
                if type(reply3) is list:
                    nestedList.append(reply3[0])
                    nestedList.append(reply3[1])
                else:
                    nestedList.append(reply3)
        except:
            pass
        
#knight 1 AI
    def appending_bN1(self):
        try:         
            A_key = self.bN1Moves[0]
            A_key = (str(A_key)[2:6])
            self.A_key = A_key
            reply = self.KnightMoves()
            nestedList = self.bN1Moves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass
        
#knight 2 AI
    def appending_bN2(self):
        try:
            A_key = self.bN2Moves[0]
            A_key = (str(A_key)[2:6])
            self.A_key = A_key
            reply = self.KnightMoves()
            nestedList = self.bN2Moves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass

#bishop 1 AI
    def appending_bB1(self):
        try:
            A_key = self.bB1Moves[0]
            self.A_key = (str(A_key)[2:6])
            reply = self.BishopMoves()
            nestedList = self.bB1Moves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass

#bishop 2 AI        
    def appending_bB2(self):
        try:
            A_key = self.bB2Moves[0]
            self.A_key = (str(A_key)[2:6])
            reply = self.BishopMoves()
            nestedList = self.bB2Moves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass
#rook 1 AI
    def appending_bR1(self):
        try:  
            A_key = self.bR1Moves[0]
            self.A_key = (str(A_key)[2:6])
            reply = self.RookMoves()
            nestedList = self.bR1Moves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass
#rook 2  AI   
    def appending_bR2(self):
        try:
            A_key = self.bR2Moves[0]
            self.A_key = (str(A_key)[2:6])
            reply = self.RookMoves()
            nestedList = self.bR2Moves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass
#queen AI
    def appending_bQ(self):
        try:
            A_key = self.bQMoves[0]
            self.A_key = (str(A_key)[2:6])
            reply = self.QueenMoves()
            nestedList = self.bQMoves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass
#king AI
    def appending_bK(self):
        try:   
            A_key = self.bKMoves[0]
            self.A_key = (str(A_key)[2:6])
            reply = self.KingMoves()
            nestedList = self.bKMoves[1]
            for element in reply:
                nestedList.append(element)
        except:
            pass
        
# Should call the Methods
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
        check = availableMoves().linearSearch()
        if check is True:
            self.existingPieces()
        else:
            self.AiUpdates()
#---------------------------------------------------------Code above is for the AI to generate all of the available moves
###---------------
#Generated a random move (AI Logic)
    def randomMove(self):
        while True:
            piece = random.randint(1, 16)
            try:
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
#King's side Rook Castling AI                       
                        if self.bKMoves[1][p] == '6, 0' and self.bKMoves[0] == '4, 0':
                            pieceValues.update({'7, 0' : None})
                            rulesDictionary.update({'7, 0' : None})
                            pieceValues.update({'5, 0' : bR})
                            rulesDictionary.update({'5, 0' : 'bR2'})
                            return [self.bKMoves[0], '6, 0']
#Queen's side Rook Castling Ai                        
                        elif self.bKMoves[1][p] == '2, 0' and self.bKMoves[0] == '4, 0':
                            pieceValues.update({'0, 0' : None})
                            rulesDictionary.update({'0, 0' : None})
                            pieceValues.update({'1, 0' : None})
                            rulesDictionary.update({'1, 0' : None})
                            pieceValues.update({'3, 0' : bR})
                            rulesDictionary.update({'3, 0' : 'bR1'})
                            return [self.bKMoves[0], '2, 0']
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
            except:
                pass

#   Updates values in the Dictionary for the AI                
    def AiUpdates(self):
        move = self.randomMove()
        Ai_From_Key = move[0][0]
        Ai_From_Value = rulesDictionary.get(move[0][0])
        Ai_From_Image = pieceValues.get(Ai_From_Key)
        Ai_To_Key = move[1]
        pieceValues.update({Ai_From_Key : None})
        rulesDictionary.update({Ai_From_Key : None})
        pieceValues.update({Ai_To_Key : Ai_From_Image})
        rulesDictionary.update({Ai_To_Key : Ai_From_Value})
        class_Rules = Rules()
        class_Rules.getStatus('user')

    def updatingElement(self, initial, coord):
        #Value stored by the coordinate previously
        previousValue = rulesDictionary.get(coord)
        #Value of the element that I am retrieving from the list
        coordValue = rulesDictionary.get(initial)
        coordImage = pieceValues.get(initial)
        rulesDictionary.update({initial : None})
        rulesDictionary.update({coord : coordValue})
        check = availableMoves().linearSearch()
        if check is True:
            rulesDictionary.update({coord : previousValue})
            rulesDictionary.update({initial : coordValue})
            return False
        else:
            pieceValues.update({initial : None})
            pieceValues.update({coord : coordImage})
            return True

    def pass_bK(self):
        count = 0
        if len(self.bKMoves[1]) > 0:
            for coord in self.bKMoves[1]:
                reply = self.updatingElement(self.bKMoves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bKMoves[1]):
                    return reply
        else:
            return False
    def pass_bQ(self):
        count = 0
        if len(self.bQMoves[1]) > 0:
            for coord in self.bQMoves[1]:
                reply = self.updatingElement(self.bQMoves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bQMoves[1]):
                    return reply
        else:
            return False
    def pass_bB2(self):
        count = 0
        if len(self.bB2Moves[1]) > 0:
            for coord in self.bB2Moves[1]:
                reply = self.updatingElement(self.bB2Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bB2Moves[1]):
                    return reply
        else:
            return False
    def pass_bB1(self):
        count = 0
        if len(self.bB1Moves[1]) > 0:
            for coord in self.bB1Moves[1]:
                reply = self.updatingElement(self.bB1Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bB1Moves[1]):
                    return reply
        else:
            return False
    def pass_bN2(self):
        count = 0
        if len(self.bN2Moves[1]) > 0:
            for coord in self.bN2Moves[1]:
                reply = self.updatingElement(self.bN2Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bN2Moves[1]):
                    return reply
        else:
            return False
    def pass_bN1(self):
        count = 0
        if len(self.bN1Moves[1]) > 0:
            for coord in self.bN1Moves[1]:
                reply = self.updatingElement(self.bN1Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bN1Moves[1]):
                    return reply
        else:
            return False
    def pass_bR2(self):
        count = 0
        if len(self.bR2Moves[1]) > 0:
            for coord in self.bR2Moves[1]:
                reply = self.updatingElement(self.bR2Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bR2Moves[1]):
                    return reply
        else:
            return False
    def pass_bR1(self):
        count = 0
        if len(self.bR1Moves[1]) > 0:
            for coord in self.bR1Moves[1]:
                reply = self.updatingElement(self.bR1Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bR1Moves[1]):
                    return reply
        else:
            return False
    def pass_bP8(self):
        count = 0
        if len(self.bP8Moves[1]) > 0:
            for coord in self.bP8Moves[1]:
                reply = self.updatingElement(self.bP8Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP8Moves[1]):
                    return reply
        else:
            return False
    def pass_bP7(self):
        count = 0
        if len(self.bP7Moves[1]) > 0:
            for coord in self.bP7Moves[1]:
                reply = self.updatingElement(self.bP7Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP7Moves[1]):
                    return reply
        else:
            return False
    def pass_bP6(self):
        count = 0
        if len(self.bP6Moves[1]) > 0:
            for coord in self.bP6Moves[1]:
                reply = self.updatingElement(self.bP6Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP6Moves[1]):
                    return reply
        else:
            return False
    def pass_bP5(self):
        count = 0
        if len(self.bP5Moves[1]) > 0:
            for coord in self.bP5Moves[1]:
                reply = self.updatingElement(self.bP5Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP5Moves[1]):
                    return reply
        else:
            return False
    def pass_bP4(self):
        count = 0
        if len(self.bP4Moves[1]) > 0:
            for coord in self.bP4Moves[1]:
                reply = self.updatingElement(self.bP4Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP4Moves[1]):
                    return reply
        else:
            return False
    def pass_bP3(self):
        count = 0
        if len(self.bP3Moves[1]) > 0:
            for coord in self.bP3Moves[1]:
                reply = self.updatingElement(self.bP3Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP3Moves[1]):
                    return reply
        else:
            return False
    def pass_bP2(self):
        count = 0
        if len(self.bP2Moves[1]) > 0:
            for coord in self.bP2Moves[1]:
                reply = self.updatingElement(self.bP2Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP2Moves[1]):
                    return reply
        else:
            return False
    def pass_bP1(self):
        count = 0
        if len(self.bP1Moves[1]) > 0:
            for coord in self.bP1Moves[1]:
                reply = self.updatingElement(self.bP1Moves[0][0], coord)
                count +=1
                if reply is True:
                    return reply
                elif reply is False and count == len(self.bP1Moves[1]):
                    return reply
        else:
            return False
    def existingPieces(self):
        found = False
        alivePieces = []
        for key, value in rulesDictionary.items():
            if value == 'bP1' or value == 'bP2' or value == 'bP3' or value == 'bP4' or value == 'bP5' or value == 'bP6' or value == 'bP7' or value == 'bP8' or value == 'bR1' or value == 'bR2' or value == 'bN1' or value == 'bN2' or value == 'bB1' or value == 'bB2' or value == 'bQ' or value == 'bK':
                alivePieces.append(value)                
        for element in reversed(alivePieces):
            if element == 'bP1' and found is False:
                found = self.pass_bP1()
            elif element == 'bP2' and found is False:
                found = self.pass_bP2()
            elif element == 'bP3' and found is False:
                found = self.pass_bP3()
            elif element == 'bP4' and found is False:
                found = self.pass_bP4()
            elif element == 'bP5' and found is False:
                found = self.pass_bP5()
            elif element == 'bP6' and found is False:
                found = self.pass_bP6()
            elif element == 'bP7' and found is False:
                found = self.pass_bP7()
            elif element == 'bP8' and found is False:
                found = self.pass_bP8()
            elif element == 'bR1' and found is False:
                found = self.pass_bR1()
            elif element == 'bR2' and found is False:
                found = self.pass_bR2()
            elif element == 'bN1' and found is False:
                found = self.pass_bN1()
            elif element == 'bN2' and found is False:
                found = self.pass_bN2()
            elif element == 'bB1' and found is False:
                found = self.pass_bB1()
            elif element == 'bB2' and found is False:
                found = self.pass_bB2()
            elif element == 'bQ' and found is False:
                found = self.pass_bQ()
            elif element == 'bK' and found is False:
                found = self.pass_bK()
            if found is True:
                break
        if found is False:
            return 'White has won the Game!'
                
                    
                

#Places the pieces on the screen
def placePieces(screen):
    for key, value in pieceValues.items():
        x_value = int((key[0:1]))/2
        y_value = int((key[3:4]))/2
        try:
            screen.blit(value, pygame.Rect(x_value*100, y_value*100, square, square))
        except:
            pass
        
    
#Main loop where the game would run
selected = []
def main():
    screen.fill((255,255,255))
    pygame.display.update()
    game_exit = False
    while not game_exit:
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                coords = [position[0]//square, position[1]//square]
                selected.append(coords)
                if len(selected) == 2:
                    if selected[1] == selected[0]:
                        selected.clear()
                        print("Unable to select the same square twice")
                if len(selected) == 2:
                    print("You have selected the square: ",selected[0])
                    print("AND")
                    print("The square: ",selected[1])
                    class_Rules = Rules()
                    class_Rules.Move()
                    selected.clear()
        drawBoard(screen)
        placePieces(screen)
        pygame.display.update()
main()
pygame.quit()
