"""Joc X si O  facut in python 
    
    Author  :Akonomy
    Version :Stable 1.2
    Last Update:18/12/2022  #menu 
    
    Press space to begin the game 

    to reset score press on it with mouse




    good luck :))                     
                                        """

import tkinter
from turtle import*
import turtle as ak
from random import*

import time 
from Controler import*
from grafica import*
from login import*


# img = tkinter.Image("photo", file="images\\cat.png")
# ak._Screen._root.iconphoto(True, img)

 #INITIALIZAREA PARAMETRILOR
        
ak.hideturtle()
main_console=Controler()
menu_console=Keyboard_keys()
getPos=Convert_click_to_pos()
graphic_console=Masa_de_joc()
login_console=Manager()
game_console=Game_data()

#time.sleep(5)
graphic_console.draw_menu()
menu_console.set_menu("ecran_meniu")



#FUNCTIA CARE RULEAZA JOCUL 

def mouse_event(x,y,player=True):

    def tester_here(x,y,data):
        x_org,y_org=x,y
        for u in range(50):
            x,y=randint(x_org-130,x_org+130),randint(y_org-50,y_org+50)
                
           # print(x,y)
            ak.pendown()
            ak.pencolor("#454545")
            ak.pensize(1)
            ak.goto(x,y)
            ak.speed(9999)

           
            if getPos.mouse_to_key(x,y,"ecran_login")==data:
                #print(test[getPos.mouse_to_key(x,y,"ecran_meniu")-12])
                ak.pencolor("green")
            else:
               # print(test[3])  
                ak.pencolor("red")  

            ak.pensize(4)
            ak.circle(2) 
            ak.penup()   
        return 0


    if menu_console.ismenu("ecran_login"):
        # graphic_console.draw_succesful_login(0)
        # tester_here(x,y,5)
        key=getPos.mouse_to_key(x,y,"ecran_login")
        if key==4:

            menu_console.set_menu("none")
            graphic_console.clear()
            graphic_console.draw_menu()
            menu_console.set_menu("ecran_meniu")

        elif key==1:
            graphic_console.draw_succesful_login(1,"outdated")
            return 0

            if login_console.autologin():
                game_data=login_console.get_data()
                #draw
                graphic_console.draw_succesful_login(1)
                return 0
            else:    
                data=graphic_console.draw_login()
                if None in data:
                    return 0

                login_console.login(data)
                game_data=login_console.get_data()

                print(game_data)
                login_console.save_game()
                login_console.keep_login()
                graphic_console.draw_succesful_login(1)

        elif key==2:
            graphic_console.draw_succesful_login(1,"outdated")
            return 0
            login_console.save_game()
            print(login_console.get_data())



        elif key==3:
            graphic_console.draw_succesful_login(1,"outdated")
            return 0
            login_console.logout()
            graphic_console.draw_succesful_login(0)
            




    if menu_console.ismenu("ecran_credits"):
        key=getPos.mouse_to_key(x,y,"ecran_credits")
        if key==15:
            menu_console.set_menu("none")
            graphic_console.clear()
            graphic_console.draw_menu()
            menu_console.set_menu("ecran_meniu")

    if menu_console.ismenu("ecran_meniu"):


        def start_game():
            graphic_console.clear()
            graphic_console.draw_score(main_console.getScore())
            main_console.resetPosition()
            ak.clear()
            graphic_console.draw_interfata()

            positions=[0,7,8,9,4,5,6,1,2,3]
            ak.bgcolor("#03060d")
            move=main_console.choseNextMove()
            time.sleep(0.2)
            graphic_console.draw(move[1],"O")
            


        key=getPos.mouse_to_key(x,y,"ecran_meniu")

        if key==12:
            menu_console.set_menu("none")
            graphic_console.clear()
            start_game()
            menu_console.set_menu("ecran_de_joc")
            menu_console.press(False)
            pass
        elif key==13:
            menu_console.set_menu("none")
            graphic_console.clear()
            graphic_console.draw_credits()
            menu_console.set_menu("ecran_credits")
            #run credits
            pass
        elif key==14:
            menu_console.set_menu("none")
            graphic_console.clear()
            graphic_console.draw_login_menu()
            menu_console.set_menu("ecran_login")
            #run login
            pass        


    elif menu_console.ismenu("ecran_de_joc"):
            

        if menu_console.ispress():
            return 0    
        
        positions=[0,1,2,3,4,5,6,7,8,9]

        if getPos.mouse_to_key(x,y,"ecran_de_joc")==10:
            game_console.reset("score")
            graphic_console.draw_score(game_console.get("score"))
            return 0

        if getPos.mouse_to_key(x,y,"ecran_credits")==15:
            menu_console.set_menu("none")
            graphic_console.clear()
            graphic_console.draw_menu()
            menu_console.set_menu("ecran_meniu")  
              
        key=graphic_console.get_mouse_click_coor(x,y)[0] 
        keys=graphic_console.get_mouse_click_coor(x,y)

          

        first_turn_is=0
                  
        def if_free_position(key):    #verifica daca pozitia e libera
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

        def is_draw():                  #verifica daca e remiza
           

            if main_console.checkif_all_ocupied():
                graphic_console.draw_win("draw")
                return "draw"    
            return False    


        def is_win():                   #verifica daca exista un castigator
            positions_convert=[0,1,5,6,7,2,3,4]
            all_check=main_console.checkifWin()
            if all_check[0]:
                pozitie_desen=all_check[1]
                castigator=all_check[2]

                return [castigator,positions_convert[pozitie_desen]]   
            return [False]
        
                
                
        def computer_move():    
            if not is_turn():

                ak.penup()
                ak.color("#0d1d29")
                move=main_console.choseNextMove()
               # print("S-a pus O pe pozitia ",move[1],positions[move[1]])
                time.sleep(0.1)
                graphic_console.draw(positions[move[1]],"O")
                
            else:
                return 0    
                
        def player_move(keys): 
            if  is_turn():
                ak.color("#0d1d29")
                ak.penup()
                
                move=main_console.markPosition(keys[0],"X")
                if move:
                    graphic_console.draw(keys[1],"X")
                    return 1

                else:
                    menu_console.press(False)
                    return 0    
            else:
                return 1        
            
        

                

        #IMPLEMENTAREA JOCULUI ->
     
        
       
        menu_console.press(True)   #pentru a bloca playerul sa mai apese x

        mutat=player_move(keys)   #MUTAREA PLAYERULUI E AICI <===

        #verify if win or draw  after player move

        if is_win()[0] or is_draw():
            game_console.increase("game_played")

            if is_draw():
                graphic_console.draw_win(is_draw()) 
                return 0

            elif is_win()[0]:

                if is_win()[0]=="X":
                    game_console.increase("player")
                elif is_win()[0]=="O":
                    game_console.increase("computer")

                graphic_console.draw_score(game_console.get("score"))    
                graphic_console.draw_win(is_win()[0])
                graphic_console.drawLine(is_win()[1])
                return 0

       

        if mutat: #verifica daca playerul a pus x pe o pozitie valida, true-> ruleaza funtia pt a pune O
            computer_move()
              


        #verify if win or draw after computer move
        if is_win()[0] or is_draw():
            game_console.increase("game_played")
            if is_draw():
                graphic_console.draw_win(is_draw()) 
                return 0

            elif is_win()[0]:

                if is_win()[0]=="X":
                    game_console.increase("player")
                elif is_win()[0]=="O":
                    game_console.increase("computer")

                graphic_console.draw_score(game_console.get("score"))     
                graphic_console.draw_win(is_win()[0])
                graphic_console.drawLine(is_win()[1])
                return 0

        menu_console.press(False)  #player can press on keys  


#KEYBOARD EVENT =====>    
def onpress_key_event(key):

    

    def exit_game(key):
        if key=="escape":
            ak.bye()
            exit()

    def reset_game(key):
        
        if key=="space" and menu_console.ismenu("ecran_de_joc"):

            graphic_console.clear(1)
            graphic_console.draw_score(game_console.get("score"))
            
            


            main_console.resetPosition()
            ak.clear()
            graphic_console.run_draw()

            positions=[0,7,8,9,4,5,6,1,2,3]
            #ak.color("#0d1d29")
            ak.bgcolor("#03060d")
            move=main_console.choseNextMove()
            time.sleep(0.2)
            graphic_console.draw(move[1],"O")

            # mas.run_draw()
            # graphic_console.draw_hitbox()
            # graphic_console.draw_hitbox([0,110],"CREDITS")
            # graphic_console.draw_hitbox([0,-110],"LOGIN")

            
            
            return True
        else:
            return False



    if reset_game(key):
        menu_console.press(False)
        return 0   
      

    elif exit_game(key):
        return 0
    return 0           



#FUNCTII PT PRELUAREA DATELOR DE INTRARE MOUSE + KEYBOARD

ak.onkeypress(lambda n="space":onpress_key_event(n),"space")
ak.onkeypress(lambda n="escape":onpress_key_event(n),"Escape")
ak.onscreenclick(mouse_event)  
ak.listen()
done()
