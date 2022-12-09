#Andrew
#19 years
#Akonomy
from turtle import*
import turtle as ak
from random import*

from Controler import*

ak.hideturtle()


class DrawSymbols:
    
    def __init__(self,name='ako'):
        self.name=name
        self.run=False
        
    def running(self,state=True):
        self.run=state
    def isrunning(self):
        return self.run
    
    def draw_win(self,player):
        ak.penup()
        ak.goto(0,120)
        ak.pendown()
        wintext="A castigat  "+player
        ak.color("red")
        ak.write(wintext,False,align="center",font=("Courier",15,"bold"))
        ak.color("black")
        ak.penup()
        
        
    def X(self,x,y):
        ak.pensize(3)
        ak.penup()    
        ak.goto(x+30,y+30)
        ak.pendown()
        ak.goto(x-30,y-30)
        ak.penup()
        ak.goto(x-30,y+30)
        ak.pendown()
        ak.goto(x+30,y-30)
        ak.penup()
        
        
    def O(self,x,y):
        ak.pensize(3)
        ak.penup()
        ak.goto(x,y-30)
        ak.pendown()
        ak.circle(30)
        ak.penup()
    
    def table(self,x=0,y=0):
        
        xpozitivMiddle=x+40
        ypozitivMiddle=y+40
        
        xpozitivMargin=x+110
        ypozitivMargin=y+110
        
        xnegativMiddle=x-40
        ynegativMiddle=y-40
        
        xnegativMargin=x-110
        ynegativMargin=y-110
        
        
        ak.pensize(4)
        ak.penup()
        ak.goto(xpozitivMiddle,ypozitivMargin)
        ak.pendown()
        ak.goto(xpozitivMiddle,ynegativMargin)
        ak.penup()
        ak.goto(xnegativMiddle,ynegativMargin)
        ak.pendown()
        ak.goto(xnegativMiddle,ypozitivMargin)
        ak.penup()
        ak.goto(xnegativMargin,ypozitivMiddle)
        ak.pendown()
        ak.goto(xpozitivMargin,ypozitivMiddle)
        ak.penup()
        ak.goto(xpozitivMargin,ynegativMiddle)
        ak.pendown()
        ak.goto(xnegativMargin,ynegativMiddle)
        ak.penup()

    def linieDiagonalaRight(self,x=0,y=0):
        ak.penup()
        ak.color("red")
        ak.pensize(3.5)
        ak.goto(x+115,y+115)
        ak.pendown()
        ak.goto(x-115,y-115)
        ak.penup()
        ak.color("black")

    def linieDiagonalaLeft(self,x=0,y=0):
        ak.penup()
        ak.color("red")
        ak.pensize(3.5)
        ak.goto(x-115,y+115)
        ak.pendown()
        ak.goto(x+115,y-115)
        ak.penup()
        ak.color("black")


    def linieOrizontala(self,line=0,x=0,y=0):
        ak.penup()
        ak.color("red")
        ak.pensize(3.5)
        if line==0:
            ak.goto(x-115,y)
            ak.pendown()
            ak.goto(x+115,y)
            ak.penup()
            
        elif line==1:
            ak.goto(x-115,y+80)
            ak.pendown()
            ak.goto(x+115,y+80)
            ak.penup()

        elif line==-1:
            ak.goto(x-115,y-80)
            ak.pendown()
            ak.goto(x+115,y-80)
            ak.penup()
            
            
    def linieVerticala(self,line=0,x=0,y=0):
        ak.penup()
        ak.color("red")
        ak.pensize(3.5)
        if line==0:
            ak.goto(x,y-115)
            ak.pendown()
            ak.goto(x,y+115)
            ak.penup()
            
        elif line==1:
            ak.goto(x+80,y-115)
            ak.pendown()
            ak.goto(x+80,y+115)
            ak.penup()

        elif line==-1:
            ak.goto(x-80,y-115)
            ak.pendown()
            ak.goto(x-80,y+115)
            ak.penup()
            
            

class KeyboardTable:
    
    def __init__(self,keys=[1,2,3,4,5,6,7,8,9]):
        self.keys=keys
        self.run=False
        
    def running (self,state=True):
        self.run=state
    def isrunning(self):
        return self.run
    
    def drawWin_message(self,symbol="X"):
        draw=DrawSymbols()
        draw.draw_win(symbol)
        
    def drawElement(self,symbol="X",keyPosition=0):
        draw=DrawSymbols()
        if symbol=="X":
            if keyPosition in self.keys:
                place=self.keys.index(keyPosition)
                
                if place==0:
                    draw.X(-80,-80)
                elif place==1:
                    draw.X(0,-80)
                elif place==2:
                    draw.X(80,-80)
                elif place==3:
                    draw.X(-80,0)    
                elif place==4:
                    draw.X(0,0)
                elif place==5:
                    draw.X(80,0)
                elif place==6:
                    draw.X(-80,80)
                elif place==7:
                    draw.X(0,80)
                elif place==8:
                    draw.X(80,80)    
                    

        elif symbol=="O":
            if keyPosition in self.keys:
                place=self.keys.index(keyPosition)
                
                if place==0:
                    draw.O(-80,-80)
                elif place==1:
                    draw.O(0,-80)
                elif place==2:
                    draw.O(80,-80)
                elif place==3:
                    draw.O(-80,0)    
                elif place==4:
                    draw.O(0,0)
                elif place==5:
                    draw.O(80,0)
                elif place==6:
                    draw.O(-80,80)
                elif place==7:
                    draw.O(0,80)
                elif place==8:
                    draw.O(80,80) 

    def UndrawElement(self,symbol="X",keyPosition=0):
        draw=DrawSymbols()
        ak.color("white")
        if symbol=="X":
            if keyPosition in self.keys:
                place=self.keys.index(keyPosition)
                
                if place==0:
                    draw.X(-80,-80)
                elif place==1:
                    draw.X(0,-80)
                elif place==2:
                    draw.X(80,-80)
                elif place==3:
                    draw.X(-80,0)    
                elif place==4:
                    draw.X(0,0)
                elif place==5:
                    draw.X(80,0)
                elif place==6:
                    draw.X(-80,80)
                elif place==7:
                    draw.X(0,80)
                elif place==8:
                    draw.X(80,80)    
                    

        elif symbol=="O":
            if keyPosition in self.keys:
                place=self.keys.index(keyPosition)
                
                if place==0:
                    draw.O(-80,-80)
                elif place==1:
                    draw.O(0,-80)
                elif place==2:
                    draw.O(80,-80)
                elif place==3:
                    draw.O(-80,0)    
                elif place==4:
                    draw.O(0,0)
                elif place==5:
                    draw.O(80,0)
                elif place==6:
                    draw.O(-80,80)
                elif place==7:
                    draw.O(0,80)
                elif place==8:
                    draw.O(80,80) 

        ak.color("black")




 #INITIALIZAREA PARAMETRILOR
draw=DrawSymbols()
draw.table()

keyboard_console=KeyboardTable()
main_console=Controler()




def onpress_key_event(key='1',player=True):
    positions=[0,7,8,9,4,5,6,1,2,3]
    try:
        key=positions[int(key)]     #pt optimizare un try-except ar fi bun aici
    except:
        print("not a number")
        pass
    first_turn_is=0
    def first_turn(key):
        
        if key=="X":
            first_turn_is=1
        elif key=="O":
            first_turn_is=0
            
        
        
    def if_free_position(key):
        if main_console.check(key):
            return True
        else:
            return False
        
    def is_turn():            #return 1 if x turn , 0 if o turn 
        pozitii_ocupate_x=0
        pozitii_ocupate_o=0
        for pozitie in range(1,10):
            if main_console.checkif(pozitie)=="X":
                pozitii_ocupate_x+=1;
            elif main_console.checkif(pozitie)=="O":
                pozitii_ocupate_o+=1;
                
                
        if pozitii_ocupate_x>pozitii_ocupate_o:
            return 0
        elif pozitii_ocupate_x<pozitii_ocupate_o:
            return 1
        elif pozitii_ocupate_x==pozitii_ocupate_o:
            return first_turn_is
    def is_win():
        positions_convert=[1,0,-1,-1,0,1]
        if main_console.checkifWin()[0]:
            
            pozitie_desen=main_console.checkifWin()[1]
            castigator=main_console.checkifWin()[2]
            
            
            #draw.textWin(castigator)
            if pozitie_desen==6:
                draw.linieDiagonalaLeft()
                
            elif pozitie_desen==7:
                draw.linieDiagonalaRight()
               
            elif pozitie_desen<3:
                draw.linieOrizontala(positions_convert[pozitie_desen])
                
            elif pozitie_desen>2:
                draw.linieVerticala(positions_convert[pozitie_desen])                     
                
            return castigator
        return False
    
            
            
    def computer_move():
        keyboard_console.running(True)
        move=main_console.choseNextMove()
       # print("S-a pus O pe pozitia ",move[1],positions[move[1]])
        keyboard_console.drawElement("O",positions[move[1]])
        keyboard_console.running(False)
        
    def player_move(key):
        keyboard_console.running(True)
        move=main_console.markPosition(key,"X")
       # print("S-a pus X pe pozitia ",move[1],positions[key])
        keyboard_console.drawElement("X",positions[key])
        keyboard_console.running(False)
    
    def reset_game(key):
        if key=="space":
            main_console.running(True)
            main_console.resetPosition()
            ak.clear()
            draw.table()
            main_console.running(False)
            return True
        else:
            return False
            

    #IMPLEMENTAREA JOCULUI ->


    
    
    
    if reset_game(key):
        return 0
    
#     if draw.isrunning() or keyboard_console.isrunning():
#          return 0

    
    if is_win():
        keyboard_console.running(True)
        keyboard_console.drawWin_message(is_win())
        keyboard_console.running(False)
        return 0
    player_move(key)
    #computer_move()
    if is_win():
        keyboard_console.running(True)
        keyboard_console.drawWin_message(is_win())
        keyboard_console.running(False)
        return 0
    #player_move(key)
    computer_move()
    if is_win():
        keyboard_console.running(True)
        keyboard_console.drawWin_message(is_win())
        keyboard_console.running(False)
        return 0
    
        

    #print(main_console.getTable())
    
        
        
        
    
ak.onkeypress(lambda n=1:onpress_key_event(n),"1")
ak.onkeypress(lambda n=2:onpress_key_event(n),"2")
ak.onkeypress(lambda n=3:onpress_key_event(n),"3")
ak.onkeypress(lambda n=4:onpress_key_event(n),"4")
ak.onkeypress(lambda n=5:onpress_key_event(n),"5")
ak.onkeypress(lambda n=6:onpress_key_event(n),"6")
ak.onkeypress(lambda n=7:onpress_key_event(n),"7")
ak.onkeypress(lambda n=8:onpress_key_event(n),"8")
ak.onkeypress(lambda n=9:onpress_key_event(n),"9")
ak.onkeypress(lambda n="space":onpress_key_event(n),"space")
ak.onkeypress(lambda n="X":onpress_key_event(n),"x")
ak.onkeypress(lambda n="O":onpress_key_event(n),"o")
ak.listen()



done()
        
        
        
        
        
        
        
        
        
        
# 
# for x in range(9):
#     #console=int(input("introduceti va rog O\n"))
#     #controler.markPosition(console,"O")
#     controler.choseNextMove()
#     controler.getTable()
#     print(controler.checkifWin())
#     console=int(input("introduceti va rog X\n"))
#     while not  controler.markPosition(console,"X"):
#         console=int(input("va rugam reintroduceti X\n"))
#     #controler.markPosition(console,"X")    
#     controler.getTable()
# #     if controler.checkifWin()[0]:
# #         print("Castigatorul este: " ,controler.checkifWin()[1])
# #         break
#     
    #controler.getTable()
    