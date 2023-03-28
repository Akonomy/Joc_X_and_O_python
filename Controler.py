from random import*

class Controler:
    
    def __init__(self,masa_de_joc=[0,0,0,0,0,0,0,0,0]):
        self.run=False
        self.masa_de_joc=masa_de_joc
        self.pozitii_disponibile=[1,2,3,4,5,6,7,8,9]
        self.pozitii_castigatoare=[[1,9,5],[3,7,5],            #diagonale 6 7
                                   [1,3,2],[4,5,6],[7,9,8],     #orizontale  0 1 2  
                                   [1,7,4],[2,8,5],[3,9,6]]     #verticale 3 4 5
                                              
        self.score=[0,0]
        
        self.pozitii_ocupate=[[],[]]  #0 for X  1 for O
        
                                
        
                                   
                                   

    def increaseScore(self,player):
        if player=="O":
            self.score[1]+=1
        elif player=="X":
            self.score[0]+=1

    def resetScore(self):
        self.score=[0,0]
        return True

    def getScore(self):
        return self.score


    def resetPosition(self,position=0):  #reseteaza toate pozitiile daca nu se specifica explicit , sterge pozitia specificata
        if position==0:
            self.masa_de_joc=[0,0,0,0,0,0,0,0,0]
            self.pozitii_ocupate=[[],[]]
            return True
        
        else:
            if position in self.pozitii_disponibile:
                masa_de_joc[position-1]=0
                if position in self.pozitii_ocupate[0]:
                    self.pozitii_ocupate[0].remove(position)
                if position in self.pozitii_ocupate[1]:
                    self.pozitii_ocupate[1].remove(position)
                return True
            else:
                print("Pozitie invalida , va rugam alegeti alta pozitie intre 1-9")
                return False

    def check(self,position):         #check  ==>  False if ocupied , True if free  
        if position==-1:
            if self.masa_de_joc==[0,0,0,0,0,0,0,0,0]:
                return True
            else:
                return False
        else:
    
            if position in self.pozitii_disponibile:
                if self.masa_de_joc[position-1]:
                    return False
                else:
                    return True
            else:
                print("\nPozitie de verificat invalida")
                    
    def checkif_all_ocupied(self):
        for x in range(1,10):
            if self.check(x)==True:
                return False
        return True        


    def checkifmark(self,position,player):  #return true if player symbol is found on position,  
        idJucator=0
        
        if player=="X":
            idJucator=1
        if player=="O":
            idJucator=2
        
        if position in self.pozitii_disponibile:
            if masa_de_joc[position-1]==idJucator:
                return True
            else:
                return False
        else:
            print("\nPozitie de verificat invalida")        


    def checkif(self,position):    #verifica daca pozitia e ocupata, daca e,  returneaza playerul X sau O  ,True daca e libera
        
        if position in self.pozitii_disponibile:
            if self.masa_de_joc[position-1]:
                if self.masa_de_joc[position-1]==1:
                    return "X"
                if self.masa_de_joc[position-1]==2:
                    return "O"
            else:
               # print("S-a verificat pozitia",position)
                return True
                
        else:
            return False
            #print("\nPozitie de verificat invalida (checkif)[",position,"]")        


    def getTable(self):  #pentru a rula jocul direct  in consola
        line=''
        count=-1
        for s in range(3):
            line=''
            for x in range(3):
                count+=1
                line+=str(self.masa_de_joc[count])
            print(line)
            
        return self.masa_de_joc
    
    
    def markPosition(self,position,player="O"):  #marcheaza X sau O pe o pozitie specificata
        
        if position in self.pozitii_disponibile:
            
            if self.check(position):
                if player=="X":
                    #self.pozitii_disponibile[position-1]=1
                    self.pozitii_ocupate[0].append(position)
                    self.masa_de_joc[position-1]=1
                    return "ocupata ca X"
                if player=="O":
                   # self.pozitii_disponibile[position-1]=2
                    self.pozitii_ocupate[1].append(position)
                    self.masa_de_joc[position-1]=2
                    return "ocupata ca O"
            else:
                print("Pozitia ",position,"  ocupata, va rugam alegeti alta sau resetati pozitiile")
                return False
        else:
            print("Pozitie invalida, va rugam alegeti alta pozitie din 1-9")
            return False
    
    
    
    def checkifWin(self):       #return  [False] if no win  [True , index pos , castigator] if win
        
        countX=0
        countO=0
        
        for pozitii in self.pozitii_castigatoare:
            countX=0
            countO=0
            for x in pozitii:
                
                if x in self.pozitii_ocupate[0]:
                    countX+=1
                    if countX==3:
                        return [True,self.pozitii_castigatoare.index(pozitii),"X"]
                    
                    
                if x in self.pozitii_ocupate[1]:
                    countO+=1
                    if countO==3:
                        return [True,self.pozitii_castigatoare.index(pozitii),"O"]
                    
        return [False]                    
                    
          
            
    def choseNextMove(self,randomMove=False):  #computerul alege urmatoarea mutare bazata pe masa de joc
        
        if randomMove:
            for x in range(100):
                move=randint(1,9)
                if self.check(move):
                    self.markPosition(move)
                    break
                
            return [True,move]
        else:
            
            if self.check(-1):
                move=randint(1,9)
                self.markPosition(move,"O")
                #print("yeah self.check(-1)")
                return[True,move]
            else:
                
                def ifcastig(player):   #verifica daca cineva poate castiga (ifcastig) 
                    
                    if player=="X":     #daca playerul poate castiga ->ruleaza
                        posibil_win=0
                        for poz_castigatoare_list in self.pozitii_castigatoare:
                            posibil_win=0
                            for poz_castigatoare_elm in poz_castigatoare_list:
                                if poz_castigatoare_elm in self.pozitii_ocupate[0]:
                                    posibil_win+=1
                            if posibil_win==2:
                                blocat=False
                                for posibil_blocat in poz_castigatoare_list:
                                    if self.checkif(posibil_blocat)=="O":
                                        blocat=True
                                if not blocat:
                                    return [True,poz_castigatoare_list]
                        return [False]    
                            
                    elif player=="O":   #daca computerul poate castiga ->ruleaza
                        posibil_win=0
                        for poz_castigatoare_list in self.pozitii_castigatoare:
                            posibil_win=0
                            for poz_castigatoare_elm in poz_castigatoare_list:
                                if poz_castigatoare_elm in self.pozitii_ocupate[1]:
                                    posibil_win+=1
                            if posibil_win==2:
                               blocat=False
                               for posibil_blocat in poz_castigatoare_list:
                                    if self.checkif(posibil_blocat)=="X":
                                        blocat=True

                               if not blocat:
                                  # print(poz_castigatoare_list)
                                   return [True,poz_castigatoare_list]
                        return [False]    
                            
                    else:
                        return [False]
                        

                def getNextMove(player="O"):    #daca nu exista posibili castigatori (getNextMove) ->ruleaza
                    
                    if player=="O": #computerul isi alege o pozitie din cele posibile castigatoare
                        

                        posibil_win=0
                        posibil_mutari=[]
                        for poz_castigatoare_list in self.pozitii_castigatoare:
                            posibil_win=0
                            for poz_castigatoare_elm in poz_castigatoare_list:
                                if poz_castigatoare_elm in self.pozitii_ocupate[1]:
                                    posibil_win+=1
                            if posibil_win>=1:
                                blocat=False
                                for posibil_blocat in poz_castigatoare_list:
                                    
                                    if self.checkif(posibil_blocat)=="X":
                                        blocat=True
                                if not blocat:
                                    posibil_mutari.append(poz_castigatoare_list)
                                   # print("appended",poz_castigatoare_list)
                        if len(posibil_mutari)>0:
                            #print("exista mutari posibile")
                            return [posibil_mutari[randint(0,len(posibil_mutari)-1)]]     
                        else:
                            return False
                    
                    elif player=="X":   #este implementat in cazul care se doreste X pt computer (not full)
                        posibil_win=0
                        posibil_mutari=[]
                        for poz_castigatoare_list in self.pozitii_castigatoare:
                            posibil_win=0
                            for poz_castigatoare_elm in poz_castigatoare_list:
                                if poz_castigatoare_elm in self.pozitii_ocupate[0]:
                                    posibil_win+=1
                            if posibil_win>=1:
                                blocat=False
                                for posibil_blocat in poz_castigatoare_list:
                                    
                                    if self.checkif(posibil_blocat)=="O":
                                        blocat=True
                                if not blocat:
                                    posibil_mutari.append(poz_castigatoare_list)
                                   
                        if len(posibil_mutari)>0: 
                            return posibil_mutari[randint(0,len(posibil_mutari)-1)]      #posibil eroare len too high  -1
                        else:
                            return False
                    
                
                #implementarea algoritmului de functionare
                secventa_castigatoare=ifcastig("O")
                if secventa_castigatoare[0]:   #daca computerul poate castiga ->run
                    
                    secventa_castigatoare=secventa_castigatoare[1]
                    for next_move in secventa_castigatoare:
                        if self.checkif(next_move)==True:
                            self.markPosition(next_move,"O")
                            break
                    return[True,next_move]    
                            
                elif ifcastig("X")[0]:  #daca playerul poate castiga ->run
                    
                    secventa_castigatoare=ifcastig("X")[1]
                    for next_move in secventa_castigatoare:
                        if self.checkif(next_move)==True:
                            self.markPosition(next_move,"O")
                            break
                        
                    return [True,next_move]      
                else:  #daca nimeni nu are o secventa castigatoare posibila , computerul cauta una si o urmeaza
                   # print("rip")
                    secventa_posibil_castigatoare=getNextMove()
                    if not secventa_posibil_castigatoare:
                        #print("how we get there")
                        
                        for x in range(100):
                            move=randint(0,9)
                            if self.checkif(move)==True:
                                self.markPosition(move,"O")
                                return [True,move]
                    marcat=False
                    for next_move in secventa_posibil_castigatoare:
                        if self.checkif(next_move)==True:
                            self.markPosition(next_move,"O")
                            marcat=True
                            return [True ,next_move]
                            break
                    if not marcat:
                       # print("how we get there")
                        for x in range(100):
                            move=randint(0,9)
                            if self.checkif(move)==True:
                                self.markPosition(move,"O")
                                return [True ,move]
                                
                             # eroare aici     



                        
class Keyboard_keys:

    def __init__ (self):
        self.screen=True
        self.menu="ecran_standby"

    def ispress(self):

        return self.screen

    def press(self,state) :
        self.screen=state 

    def set_menu(self,menu="ecran_de_joc"):
        self.menu=menu

    def ismenu(self,menu="ecran_de_joc"):
        if self.menu==menu:
            return True
        else:
            return False    
        

        

class Convert_click_to_pos:

    def __init__(self):
        self.pos=[0,7,8,9,4,
                  5,6,1,2,3,
                  10,11,12,13,14,
                  15]


    def mouse_to_key(self,x=413,y=207,menu="ecran_de_joc"):   # convert mouse to keys
        limit_middle=40
        limit_margin=120
        limit_middle_negativ=-40
        limit_margin_negativ=-120

        #case-uri de verificare locul unde s-a efectuat click cu mouse-ul ==>
            #CASE 7

        if menu=="ecran_de_joc":
                
            if x<limit_middle_negativ-2 and x>limit_margin_negativ+2:
                if y>limit_middle+2  and y <limit_margin-2:
                    return self.pos[7]

            

                #CASE 8
            if x>limit_middle_negativ+2 and x<limit_middle-2:
                if y>limit_middle+2  and y <limit_margin-2:
                    return self.pos[8]

         


                #CASE 9
            if x>limit_middle+2 and x<limit_margin-2:
                if y>limit_middle+2  and y <limit_margin-2:
                    return self.pos[9]
                else:
                    pass


                #CASE 4
            if x<limit_middle_negativ-2 and x>limit_margin_negativ+2:
                if y>limit_middle_negativ+2  and y <limit_middle-2:
                    return self.pos[4]
                else:
                    pass


                #CASE 5    
            if x>limit_middle_negativ+2 and x<limit_middle-2:
                if y>limit_middle_negativ+2  and y <limit_middle-2:
                    return self.pos[5]
                else:
                    pass
         

                #CASE 6    
            if x>limit_middle+2 and x<limit_margin-2:
                if y>limit_middle_negativ+2  and y <limit_middle-2:
                    return self.pos[6]
                else:
                    pass


                #CASE 1
            if x<limit_middle_negativ-2 and x>limit_margin_negativ+2:
                if y<limit_middle_negativ-2  and y >limit_margin_negativ+2:
                    return self.pos[1]
                else:
                    pass
         

                #CASE 2    
            if x>limit_middle_negativ+2 and x<limit_middle-2:
                if y<limit_middle_negativ-2  and y >limit_margin_negativ+2:
                    return self.pos[2]
                else:
                    pass


                #CASE 3    
            if x>limit_middle+2 and x<limit_margin-2:
                if y<limit_middle_negativ-2  and y >limit_margin_negativ+2:
                    return self.pos[3]
                else:
                    pass


                #SPECIALS 


                #RESET SCORE POS
            if x>95 and x<315 :
                if y>205 and y<245:
                    return self.pos[10]
                else:
                    pass

                
                #BACK TO MENU
                
            if x>-300 and x<-180 :
                if y>205 and y<245:
                    return self.pos[11]
                else:
                    pass     
            else:
                return 0  
        

        elif menu=="ecran_meniu":
            button_pressed=-1
            coords=[[0,0],[0,110],[0,-110]]
            #coords=[start,credits,login] //ordinea butoanelor din lista de sus
            for coordonate_disponibile in coords:
                xlimit,ylimit=coordonate_disponibile 

                if x>xlimit-195 and x<xlimit+195:
                    if y>ylimit-95 and y<ylimit-5:
                        button_pressed=coords.index(coordonate_disponibile)
                        break


            if button_pressed==0:
                return self.pos[12] #start
            elif button_pressed==1:
                return self.pos[13] #credits
            elif button_pressed==2:
                return self.pos[14] #login
            else:
                return -413    

        elif menu=="ecran_credits":
        
            coords=[-350,500]   

            xlimit,ylimit=coords
            if x>(xlimit-195)*0.5 and x<(xlimit+195)*0.5:
                if y>(ylimit-95)*0.5 and y<(ylimit-5)*0.5:
                    return self.pos[15]
            return -1


        elif menu=="ecran_login":
        
            coords=[-180,180,200]

            if x>-180 and x<180:
                if y< 160  and y> 70: 
                    return 1
            if x>-180 and x<180:
                if y< 45  and y> -45: 
                    return 2
            if x>-180 and x<180:
                if y< -70  and y> -160: 
                    return 3

            if x<-155 and x>-300:
                if y<250 and y>200:
                    return 4        

            if x>155 and x<300:
                if y<250 and y>200:
                    return 5        
            return 0        



class Game_data:

    def __init__(self):
        self.time=0
        self.player_win=0
        self.computer_win=0
        self.draw=0
        self.game_played=0

    def get(self,data):
        if data=="all":
            return self.player_win,self.computer_win,self.time
             
        elif data=="player":
            return self.player_win 
        elif data=="computer":
            return self.computer_win
        elif data=="score":
            return[self.player_win,self.computer_win]    
        elif data=="time":
            return self.time
        elif data=="game_played":
            return self.game_played    

    def increase(self,data,value=None):
        if value==None:
            value=1


        if data=="player":
            self.player_win+=value 
        elif data=="computer":
            self.computer_win+=value
        elif data=="time":
            self.time+=value
        elif data=="game_played":
            self.game_played+=value




    def reset(self,data,value=None):
        if value==None:
            value=0


        if data=="player":
            self.player_win=value 
        elif data=="computer":
            self.computer_win=value
        elif data=="time":
            self.time=value  
        elif data=="game_played":
            self.game_played=value
        elif data=="score":
            self.player_win,self.computer_win=0,0    






