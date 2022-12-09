from random import*

class Controler:
    
    def __init__(self,masa_de_joc=[0,0,0,0,0,0,0,0,0]):
        self.run=False
        self.masa_de_joc=masa_de_joc
        self.pozitii_disponibile=[1,2,3,4,5,6,7,8,9]
        self.pozitii_castigatoare=[[1,3,2],[4,5,6],[7,9,8],     #orizontale  0 1 2  
                                   [1,7,4],[2,8,5],[3,9,6],     #verticale 3 4 5
                                   [1,9,5],[3,7,5]]             #diagonale 6 7
        
        
        self.pozitii_ocupate=[[],[]]  #0 for X  1 for O
        
                                
        
                                   
                                   
    def running(self,state=True):
        self.run=state
        
    def isrunning(self):
        return self.run
    
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


    def getTable(self):
        line=''
        count=-1
        for s in range(3):
            line=''
            for x in range(3):
                count+=1
                line+=str(self.masa_de_joc[count])
            print(line)
            
        return self.masa_de_joc
    
    
    def markPosition(self,position,player="O"):
        
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
                    
          
            
    def choseNextMove(self,randomMove=False):
        
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
                
                def ifcastig(player):
                    
                    if player=="X":
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
                            
                    elif player=="O":
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
                        

                def getNextMove(player="O"):
                    
                    if player=="O":
                        
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
                            return [posibil_mutari[randint(0,len(posibil_mutari)-1)]]      #posibil eroare len too high  -1
                        else:
                            return False
                    
                    elif player=="X":
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
                    
                
                secventa_castigatoare=ifcastig("O")
                if secventa_castigatoare[0]:
                    
                    secventa_castigatoare=secventa_castigatoare[1]
                    for next_move in secventa_castigatoare:
                        if self.checkif(next_move)==True:
                            self.markPosition(next_move,"O")
                            break
                    return[True,next_move]    
                            
                elif ifcastig("X")[0]:
                    
                    secventa_castigatoare=ifcastig("X")[1]
                    for next_move in secventa_castigatoare:
                        if self.checkif(next_move)==True:
                            self.markPosition(next_move,"O")
                            break
                        
                    return [True,next_move]      
                else:
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
                        

        