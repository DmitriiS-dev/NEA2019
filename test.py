import pygame
#Initialise pygame
pygame.init()
#tkinter:
from tkinter import *

#The board colours
white = (235,235,208)
green = (119,148,85)

#Dimensions for the board
dimension = 8
height = 400
width = 400
square = height // dimension

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

#Dictionary
pieceValues = {'0, 0': bR, '1, 0': bN, '2, 0': bB, '3, 0': bQ, '4, 0': bK, '5, 0': bB, '6, 0': bN, '7, 0': bR,
                '0, 1': bP, '1, 1': bP, '2, 1': bP, '3, 1': bP, '4, 1': bP, '5, 1': bP, '6, 1': bP, '7, 1': bP,
                '0, 2': None, '1, 2': None, '2, 2': None, '3, 2': None, '4, 2': None, '5, 2': None, '6, 2': None, '7, 2': None,
                '0, 3': None, '1, 3': None, '2, 3': None, '3, 3': None, '4, 3': None, '5, 3': None, '6, 3': None, '7, 3': None,
                '0, 4': None, '1, 4': None, '2, 4': None, '3, 4': None, '4, 4': None, '5, 4': None, '6, 4': None, '7, 4': None,
                '0, 5': None, '1, 5': None, '2, 5': None, '3, 5': None, '4, 5': None, '5, 5': None, '6, 5': None, '7, 5': None,
                '0, 6': wP, '1, 6': wP, '2, 6': wP, '3, 6': wP, '4, 6': wP, '5, 6': wP, '6, 6': wP, '7, 6': wP,
                '0, 7': wR, '1, 7': wN, '2, 7': wB, '3, 7': wQ, '4, 7': wK, '5, 7': wB, '6, 7': wN, '7, 7': wR}

rulesDictionary ={'0, 0': 'bR', '1, 0': 'bN', '2, 0': 'bB', '3, 0': 'bQ', '4, 0': 'bK', '5, 0': 'bB', '6, 0': 'bN', '7, 0': 'bR',
                  '0, 1': 'bP', '1, 1': 'bP', '2, 1': 'bP', '3, 1': 'bP', '4, 1': 'bP', '5, 1': 'bP', '6, 1': 'bP', '7, 1': 'bP',
                  '0, 2': None, '1, 2': None, '2, 2': None, '3, 2': None, '4, 2': None, '5, 2': None, '6, 2': None, '7, 2': None,
                  '0, 3': None, '1, 3': None, '2, 3': None, '3, 3': None, '4, 3': None, '5, 3': None, '6, 3': None, '7, 3': None,
                  '0, 4': None, '1, 4': None, '2, 4': None, '3, 4': None, '4, 4': None, '5, 4': None, '6, 4': None, '7, 4': None,
                  '0, 5': None, '1, 5': None, '2, 5': None, '3, 5': None, '4, 5': None, '5, 5': None, '6, 5': None, '7, 5': None,
                  '0, 6': 'wP', '1, 6': 'wP', '2, 6': 'wP', '3, 6': 'wP', '4, 6': 'wP', '5, 6': 'wP', '6, 6': 'wP', '7, 6': 'wP',
                  '0, 7': 'wR', '1, 7': 'wN', '2, 7': 'wB', '3, 7': 'wQ', '4, 7': 'wK', '5, 7': 'wB', '6, 7': 'wN', '7, 7': 'wR'}

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

#Validates Moves and Updates dictionary
class Rules():
#Initialise the class and write down the variables which would be accessed by many subroutines:
    def __init__(self):
        self.validMove = False
        self.from_Key = str(selected[0][0]) + ',' + ' ' + str(selected[0][1])
        self.to_Key = str(selected[1][0]) + ',' + ' ' + str(selected[1][1])
        self.Move2 = rulesDictionary.get(self.from_Key)
        self.Take2 = rulesDictionary.get(self.to_Key)
        print(self.Move2)
        print(self.to_Key)
        
    def Move(self):
        
        def upgrade(self):
        #This code is going to be edited to a pop up window
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
            return 'You cannot Move the Black pieces when playing as White!', self.validMove
#RULE 2:          
        def attemptTakeWhitePiece(self):
            self.validMove = False
#   Here will be code for a pop up window
            return "You can not take the same coloured piece as your own", self.validMove
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
                    if rulesDictionary.get('1, 7') is None and rulesDictionary.get('3, 7') is None and rulesDictionary.get('0, 7') == 'wR'and rulesDictionary.get('2, 7') is None:
                        self.validMove = True
                        pieceValues.update({'0, 7' : None})
                        rulesDictionary.update({'0, 7' : None})
                        rulesDictionary.update({'3, 7' : 'wR'})
                        pieceValues.update({'3, 7' : wR})
                elif self.to_Key == '6, 7' and self.from_Key == '4, 7':
                    if rulesDictionary.get('6, 7') == None and rulesDictionary.get('5, 7') == None and rulesDictionary.get('7, 7') == 'wR':
                        self.validMove = True
                        pieceValues.update({'7, 7' : None})
                        rulesDictionary.update({'7, 7' : None})
                        rulesDictionary.update({'5, 7' : 'wR'})
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
###--------------
        def diagonally(self):
            count = int(self.from_Key[0:1])
            count2 = int(self.from_Key[3:4])
            while count != int(self.to_Key[0:1]):
#           count changes to move right_up:
                if count < int(self.to_Key[0:1]) and count2 > int(self.to_Key[3:4]):
                    count +=1
                    count2 -=1
#           count changes to move left_down:
                elif count > int(self.to_Key[0:1]) and count2 < int(self.to_Key[3:4]):
                    count -=1
                    count2 +=1
#           count changes to move left_up:
                elif count > int(self.to_Key[0:1]) and count2 > int(self.to_Key[3:4]):
                    count -=1
                    count2 -=1
#           count changes to move right_down
                elif count < int(self.to_Key[0:1]) and count2 < int(self.to_Key[3:4]):
                    count +=1
                    count2 +=1
                if rulesDictionary.get(str(count)+', '+str(count2)) != None:
                        self.validMove = False
                        break
                if count == int(self.to_Key[0:1]) and count2 == int(self.to_Key[3:4]):
                    self.validMove = True
            return self.validMove
###--------------
        
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
                if upgrade1 == 'wP':
                    upgrade(self)
                else:
                    pass
                
    #RULE 1:Prevents user moving Black pieces
        if self.Move2[0:1] == 'b':
            attemptMoveAsBlack(self)

    #RULE 2: Prevents user taking their own pieces (white)
        elif self.Take2 is not None and self.Take2[0:1] == 'w':
            attemptTakeWhitePiece(self)

    #Pawn:
        elif self.Move2 == 'wP':
            pawn(self)

    #RULE 5: Valid move for Knight
        elif self.Move2 == 'wN':
            knight(self)
                        
    #RULE 6: Valid move for Bishop
        elif self.Move2 == 'wB':
            bishop(self)

    #RULE 7: Valid move for Rook
        elif self.Move2 == 'wR':
            rook(self)
                        
    #RULE 8: Valid move for Queen
        elif self.Move2 == 'wQ':
            queen(self)

    #RULE 9: Valid move for King
        elif self.Move2 == 'wK':
            king(self)
                        
        if self.validMove == True:
            pieceUpdate(self)
        

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
    screen = pygame.display.set_mode((width,height))
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
#Edit this part so the whole move validator is here
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
