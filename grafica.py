from turtle import*
from random import*
import turtle as ako

import tkinter



ako.title("GAME")
#img = tkinter.Image("photo", file="images\\cat.png")
#ako._Screen._root.iconphoto(True, img)
ako.bgcolor("#03060d")
text=ako.Turtle()
score=ako.Turtle()

score.ht()
text.ht()

#pt symboluri x sau o  symo-x  symon=o
symo=ako.Turtle()  
symo.ht()
symo.speed(3)

symon=ako.Turtle()
symon.ht()
symon.speed(3)

hitbox=ako.Turtle()
hitbox.ht()
hitbox.speed(3)
hitbox.pencolor("green")

credits=ako.Turtle()
credits.ht()
credits.speed(3)
credits.penup()

lines=ako.Turtle()
lines.ht()
lines.speed(3)
lines.penup()


login=ako.Turtle()
login.ht()
login.speed(3)
login.penup()

task=ako.Turtle()
task.ht()
task.speed(3)
task.penup()






class Masa_de_joc:

    def __init__(self):
        self.size_cube=120
        self.tabla={}
        self.red=randint(20,30)
        self.blue=200
        self.green=randint(0,15)
        self.gameText=False
        ako.ht()
        

    def run_draw(self):

        ako.bgcolor("#03060d")
        ako.color("white")
        #ako.hideturtle()
        ako.colormode(255)
        ako.speed(9999)
        ako.clear()
        ako.pensize(1)

        

        red=180
        blue=200
        green=0
        increase_green=randint(5,25)
        descrease_blue=randint(4,10)


        
        size_cube=120  #dimensiunea cubului //
        count=-2.5  #pentru x, se observa ca x=count 
        for z in range(1,2):
            for x in range(-1,2):   #loop generare  masa de joc
                count+=1
                for y in range(-1,2):
                    

                    #COLOR PICKER

                    if green<230:
                        green+=increase_green
                        if red>20:
                            green-=1
                            red-=20

                    if blue>descrease_blue:
                        blue-=descrease_blue

                        
                    ako.color(red,green,blue) 


                    #DRAW POLY
                    x=count

                    ako.penup()
                    ako.goto(x*size_cube,(y-1)*size_cube)
                    ako.pendown()
                    
                    #ako.clear()
                    ako.pendown()
                    ako.begin_poly()
                    ako.goto(x*size_cube,y*size_cube)
                    ako.goto((x+1)*size_cube,y*size_cube)
                    ako.goto((x+1)*size_cube,(y-1)*size_cube)
                    ako.goto(x*size_cube,(y-1)*size_cube)
                    ako.end_poly()
                    ako.penup()

                    self.tabla[str(str(x)+":"+str(y))]=ako.get_poly()
                    ako.getscreen().update() 
        ako.speed(3) 
                  
        return 0            
    
    def get_mouse_click_coor(self,x, y):
        # print(x, y)

    
        for n in self.tabla.keys():
            if x>self.tabla[n][0][0] and  x<self.tabla[n][2][0]:
                if y> self.tabla[n][0][1] and y<self.tabla[n][2][1]:
                    # print(n)

                    if n =="-1.5:1":
                        return [1,n]
                    elif n=="-0.5:1":
                        return [2,n]  

                    elif n=="0.5:1":
                        return [3,n] 

                    elif n=="-1.5:0":
                        return [4,n] 

                    elif n=="-0.5:0":
                        return [5,n] 

                    elif n=="0.5:0":
                        return [6,n] 

                    elif n=="-1.5:-1":
                        return [7,n] 

                    elif n=="-0.5:-1":
                        return [8,n]       
                    
                    elif n=="0.5:-1":
                        return [9,n] 

    
    def draw(self,poly,symbol):



  
        if len(str(poly))==1:

            n=int(poly)

            if n ==1:
                poly="-1.5:1"

            elif n==2:
                poly="-0.5:1" 

            elif n==3:
                poly="0.5:1" 

            elif n==4:
                poly="-1.5:0"

            elif n==5:
                poly="-0.5:0"

            elif n==6:
                poly="0.5:0"

            elif n==7:
                poly="-1.5:-1"

            elif n==8:
                poly="-0.5:-1"

            elif n==9:
                poly="0.5:-1"    


        x=float(poly.split(":")[0])
        y=float(poly.split(":")[1])

        


        increase_green=randint(5,5)
        descrease_blue=randint(2,5)
        size_cube=120  #dimensiunea cubului //

        y-=1
                
        #COLOR PICKER

        if self.green<230:
            self.green+=increase_green
            if self.red>20:
                self.green-=1
                self.red-=20
        if self.green>=230:
            if self.red+15<256:
                self.red+=15

        if self.blue>descrease_blue:
            self.blue-=descrease_blue
        ako.colormode(255)
        symo.color(self.red,self.green,self.blue) 
        symon.color(self.red,self.green,self.blue)


        if symbol=="O":


            symon.pensize(3)
            symon.penup()
            symon.speed(99999)
            symon.goto((x+0.5)*size_cube,(y+0.1)*size_cube)
            symon.pendown()
            symon.circle(45)
            symon.speed(3)
            symon.penup()
    
    
        #DRAW POLY  X
        if symbol=="X":

            symo.pensize(3)
            symo.penup()
            symo.goto((x+0.2)*size_cube,(y+0.2)*size_cube)
            symo.pendown()
            
            #ako.clear()
            symo.pendown()
            symo.goto((x+0.2)*size_cube,(y+0.2)*size_cube)
            symo.goto((x+0.8)*size_cube,(y+0.8)*size_cube)
            symo.penup()
            symo.goto((x+0.2)*size_cube,(y+0.8)*size_cube)
            symo.pendown()
            symo.goto((x+0.8)*size_cube,(y+0.2)*size_cube)


 
    def drawLine(self,line):
        x=1
        y=1
        def run(x,y,size,draw=False):
            lines.pensize(2)
            if draw: 
                lines.pendown()
            else:
                lines.penup()    

            lines.pencolor("cyan")
            lines.goto(x*size,y*size)
            lines.penup()
  

        if line==0:             #linie diagonala right
            x=-1.5
            y=1
            run(x,y,125,False)
            x=1.5
            y=-2
            run(x,y,125,True)

        elif line==1:           #linie diagonala left
            x=1.5
            y=1
            run(x,y,125,False)
            x=-1.5
            y=-2
            run(x,y,125,True)

        elif line==2:       #linie verticala left
            x=-0.95
            y=1
            run(x,y,125,False)
            x=-0.95
            y=-2
            run(x,y,125,True)


        elif line==3:       #linie verticala middle
            x=0
            y=1
            run(x,y,125,False)
            x=0
            y=-2
            run(x,y,125,True)



        elif line==4:       #linie verticala right
            x=0.95
            y=1
            run(x,y,125,False)
            x=0.95
            y=-2
            run(x,y,125,True)


        elif line==5:       #linie orizontala top
            x=-1.5
            y=0.5
            run(x,y,125,False)
            x=1.5
            y=0.5
            run(x,y,125,True)


        elif line==6:       #linie orizontala middle
            x=-1.5
            y=-0.5
            run(x,y,125,False)
            x=1.5
            y=-0.5
            run(x,y,125,True)


        elif line==7:       #linie orizontala bottom
            x=-1.5
            y=-1.5
            run(x,y,125,False)
            x=1.5
            y=-1.5
            run(x,y,125,True)



    def clear(self,mode=0):
        if not mode:
            ako.clear()
            text.clear()
            symo.clear()
            score.clear()
            symon.clear()
            hitbox.clear()
            credits.clear()
            lines.clear()
            login.clear()
            task.clear()
        elif mode==1:
            text.clear()
            symo.clear()
            symon.clear()
            lines.clear()
            task.clear()




    def draw_win(self,player):  #deseneaza textul pentru ecranul de castig
        text.clear()
        text.penup()
        text.goto(0,120)
        text.pendown()
        text.color("#0eb9c7")
        wintext=""
        if player=="O":
            text.color("#0eb1c7")
            wintext="A castigat computerul ,ups"
        elif player=="X":
            text.color("#0eb1c7")
            wintext="Ai castigat , yay"    
        elif player=="draw":
            text.color("#54300a")
            wintext="Remiza "    

        
        text.write(wintext,False,align="center",font=("Courier",15,"bold"))
        text.penup()




    def draw_score(self,scor):  #deseneaza scorul
        color="cyan"
        if scor[1]>scor[0]:
            color="#45399f"
        #print(scor)

        score.color(color)        
        score.penup()
        score.goto(200,200)
        
        wintext=str(scor[0])+"   -   "+str(scor[1])
        score.clear()
        score.write(wintext,False,align="center",font=("Courier",15,"bold"))
        score.goto(200,218)    
        score.write("  player vs computer ",False,align="center",font=("Courier",15,"bold"))
        score.penup()

    def draw_hitbox(self,place=[0,0],text="START",muxy_=1,muxx_=1):
        muxy=muxy_  #multiplicator pentru definirea raportului 
        muxx=muxx_  #multiplicator x pt definirea raportului
        x,y=place
        hitbox.speed(5)
        hitbox.penup()
        hitbox.goto(muxx*(x+0),muxy*(y-150))
        hitbox.pensize(1)
        hitbox.pencolor("#0fffff")
        hitbox.write(  text+"\n",False,align="center",font=("Terminator Two",int(50*muxx),"bold"))
        hitbox.pencolor("#143535")
        hitbox.write(  text+"\n",False,align="center",font=("Terminator Two",int(50*muxx)))
      
         

        hitbox.pencolor("cyan")
        hitbox.pensize(5)
        hitbox.penup()
        hitbox.goto((x+180)*muxx,(y)*muxy)
        hitbox.pendown()
        hitbox.goto((x+200)*muxx,(y-20)*muxy)
        hitbox.goto((x+200)*muxx,(y-80)*muxy)
        hitbox.goto((x+180)*muxx,(y-100)*muxy)
        #left
        
        hitbox.goto((x-180)*muxx,(y-100)*muxy)
        hitbox.goto((x-200)*muxx,(y-80)*muxy)
        hitbox.goto((x-200)*muxx,(y-20)*muxy)
        hitbox.goto((x-180)*muxx,(y)*muxy)
        hitbox.goto((x+180)*muxx,(y)*muxy)

        hitbox.speed(413)
        hitbox.pencolor("#365957")
        hitbox.pensize(3)
        hitbox.penup()
        hitbox.goto((x+178)*muxx,(y-2)*muxy)
        hitbox.pendown()    
        
        hitbox.goto((x+198)*muxx,(y-22)*muxy)
        hitbox.goto((x+198)*muxx,(y-78)*muxy)
        hitbox.goto((x+178)*muxx,(y-98)*muxy)
        #left
        hitbox.goto((x-178)*muxx,(y-98)*muxy)
        hitbox.goto((x-198)*muxx,(y-78)*muxy)
        hitbox.goto((x-198)*muxx,(y-22)*muxy)
        hitbox.goto((x-178)*muxx,(y-2)*muxy)
        hitbox.goto((x+178)*muxx,(y-2)*muxy)



    def draw_menu(self):
        ako.getscreen().tracer(2,2)

        self.draw_hitbox()
        self.draw_hitbox([0,110],"CREDITS")
        self.draw_hitbox([0,-110],"LOGIN")

        ako.getscreen().tracer(1,2)

        return True


    def draw_credits(self):
        
        self.clear()
        credits.pencolor("cyan")

        credit_text="""ThAnks for plAying!\n\nDeveloped by: akonomy
version 1.2\n\nFeedback:\nakonomy.official@gmail.com\n\nLicense: MPL-2.0
                    """
        credits.goto(0,-200)
        credits.write(credit_text+"\n",False,align="center",font=("Terminator Two",20,"bold"))

        self.draw_hitbox([-350,500],"back",0.5,0.5)


    def draw_interfata(self):

        self.draw_hitbox([-350,500],"back",0.5,0.5)
        self.run_draw()






    def draw_sign_up(self):
        data_catch=["username","password"]

        for x in range(2):
            data_catch[x]=ako.textinput("Register","Please choose a "+str(data_catch[x]))
        return data_catch 

    def draw_login(self):
        data_catch=["username","password"]

        for x in range(2):
            data_catch[x]=ako.textinput("Login","Please insert "+str(data_catch[x]))
        return data_catch 
               

    def draw_login_menu(self):
    
        def runtext(text,size_font,x=None,y=None):
                x_temp,y_temp=login.pos()
                x_go,y_go=x_temp,y_temp
                if x != None:
                    x_go=x_temp+x
                if y !=None:
                    y_go=y_temp+y
                login.penup()
                login.goto(x_go,y_go)  
                login.pendown()      
                login.write(text+"\n",False,align="center",font=("Terminator Two",size_font,"bold"))
                login.penup()
                login.goto(x_temp,y_temp)
                login.pendown()
                return 0


                
        def run(x,y,draw=False):
            login.getscreen().tracer(1,0)
            login.pensize(2)
            if draw: 
                login.pendown()
            else:
                login.penup()    

            login.pencolor("cyan")
            login.goto(x,y)
            login.penup()


        # login.pencolor("cyan")
        # login.penup()
        # login.goto(300,0)
        # login.pendown()
        # login.goto(300,250)
        # login.goto(-300,250)
        # login.goto(-300,-250)
        # login.goto(300,-250)
        # login.goto(300,250)





        # run(-180,-200,False)
        # run(-180,200,True)
        # run(180,200,True)
        # run(180,-200,True)
        # run(-180,-200,True)


        # run(0,160)
        # run(0,70,True)
        # run(0,45)
        # run(0,-45,True)
        # run(0,-70)
        # run(0,-160,True)



        ##down top
        run(-170,160)
        run(-180,150,True)
        run(-180,80,True)
        run(-170,70,True)
        run(0,70,True)
        runtext("Login",35,None,-25) 
        run(170,70,True)


        ##down middle
        run(170,45)
        run(180,35,True)
        run(180,-35,True)
        run(170,-45,True)
        run(170,-45,True)
        run(0,-45,True)
        runtext("Settings",35,None,-25)
        run(-170,-45,True)

        ##down bottom
        run(-170,-70)
        run(-180,-80,True)
        run(-180,-150,True)
        run(-170,-160,True)
        run(0,-160,True)
        runtext("Statistics",35,None,-25)
        run(170,-160,True)

        ##up bottom
        run(180,-150,True)
        run(180,-80,True)
        run(170,-70,True)
        run(-170,-70,True)

        ##up middle
        run(-170,-45)
        run(-180,-35,True)
        run(-180,35,True)
        run(-170,45,True)
        run(170,45,True)

        #up top
        run(170,70)
        run(180,80,True)
        run(180,150,True)
        run(170,160,True)
        run(-170,160,True)



        #close box


        run(-150,200)
        run(-290,200,True)
        run(-300,210,True)
        run(-300,240,True)
        run(-290,250,True)

        run(-240,250,True)
        runtext("back",20,15,-65)

        run(-150,250,True)
        run(-160,240,True)
        run(-160,210,True)
        run(-150,200,True)  



        login.getscreen().update()  


    def draw_succesful_login(self,data,name="log"):




        COLOR=["#2c3e50", "#34495e", "#2c3e50", "#1f3a93", "#1a237e", "#283593", "#3949ab", "#303f9f","#0097a7",
         "#00838f", "#006064", "#00695c", "#2e7d32", "#1b5e20", "#33691e", "#558b2f","#9e9d24", "#f9a825", 
         "#ff8f00", "#ef6c00", "#d84315", "#4e342e", "#5d4037", "#6d4c41","#795548", "#8d6e63", "#bdbdbd", 
         "#757575", "#616161", "#424242", "#212121", "#b2dfdb","#80cbc4", "#4db6ac", "#26a69a", "#009688",
          "#00897b", "#00796b", "#00695c", "#004d40","#43a047", "#388e3c", "#2e7d32", "#1b5e20", "#689f38",
           "#558b2f", "#33691e", "#ef5350","#e53935", "#c62828", "#b71c1c", "#d81b60", "#c2185b", "#880e4f",
            "#8e24aa", "#6a1b9a","#4a148c", "#3f51b5", "#303f9f", "#1976d2", "#0277bd", "#00838f", "#006064"]


        TIPS=[  

        "Ai un talent incontestabil...\n la a face ceva din nimic.",
        "Nu-i bai, ai reusit macar sa\n  te trezesti la timp azi.",
        "Niciodata nu esti singur cand ai probleme,\n  intotdeauna exista cineva dispus\n  sa-ti ofere un sfat inutil.",
        "Poti face orice iti doresti in viata,\n  atat timp cat nu necesita\n  abilitati sau talent.",
        "Fii mandru de tine, \n esti unic in felul tau. \n La fel ca toti ceilalti.",
        "Viata este ca o cutie de ciocolata...\n  niciodata nu stii ce primesti,\n  dar sigur nu e ceea ce-ti doresti.",
        "Nu-ti face griji daca iti merge greu.\n  Daca ai stat suficient de mult pe loc,\n  incepi sa cresti radacini.",
        "Nu te ingrijora ca esti diferit.\n  Cand toti ceilalti sunt la fel,\n  te poti considera special.\n ",
        "Succesul vine la cei\n  care isi urmaresc cu tenacitate obiectivele...\n  sau cel putin asta le spunem copiilor.\n ",
        "Nu te ingrijora,\n  lucrurile se vor imbunatati.\n  Sau nu, cine stie?\n ",
        "Viata e o ruleta ruseasca, \n tine-ti capul sus si\n  spera ca nu esti urmatorul.",
        "Lasa ca marea mai are pesti,\n  dar tu esti in mijlocul desertului\n ",
        "In viata mai si castigi",
        "Tu chiar stai sa citesti astea?",
        "In loc sa faci ceva productiv\n  apesi pe butoane sa vezi ce mai pica",
        "Ha ha ha, si credeam \n ca o sa fie o idee buna",
        "Apasa space pentru a continua jocul",
        "In viata mai si pierzi",
        "Te iubesc",
        "Oricum si maine va fi rau,\n  de ce iti faci griji?",
        "Depinde de tine",
        "Invata, adapteaza, \n devino cel mai bun",
        "Fiecare zi este o noua sansa",
        "Esti o persoana valoroasa",
        "Succesul este posibil pentru tine",
        "Sanatatea este cea mai mare bogatie",
        "Ai un viitor stralucit",
        "Oamenii te iubesc si te apreciaza",
        "Exista mereu speranta",
        "Mai sunt multe lucruri bune\n care vor veni",
        "Fii recunoscator\n  pentru ceea ce ai acum",
        "Invata sa te bucuri de fiecare moment",
        "Sa fii fericit \n este o alegere \n pe care o poti face",
        "Fiecare zi este o oportunitate\n  de a invata ceva nou",
        "Iti poti atinge obiectivele\n  daca muncesti din greu",
        "Iubeste-te pe tine insuti si pe altii",
        "Fii deschis \n la noi experiente si oportunitati",       
        "Fa o diferenta pozitiva \n in lumea inconjuratoare",
        "Zambeste, razi si bucura-te de viata",
        "Am un noroc..\n  se prabuseste blocu\n  inainte sa ajung in varfu lui",
        "Bine daca nu aveam restante era bine..\n  dar bineinteles ca nu s-a putut",
        "Sfantu 5",
        "Incearca, nu se stie niciodata",
        "Atata s-a putut ",]


        fun_txt= TIPS[randint(0,43)]         
        color=COLOR[randint(0,55)]    
        def runtext(text,size_font,x=None,y=None):
                x_temp,y_temp=task.pos()
                x_go,y_go=x_temp,y_temp
                if x != None:
                    x_go=x_temp+x
                if y !=None:
                    y_go=y_temp+y
                task.penup()
                task.goto(x_go,y_go)  
                task.pendown()      
                task.write(text+"\n",False,align="center",font=("arial",size_font,"bold"))
                task.penup()
                task.goto(x_temp,y_temp)
                task.pendown()
                return 0


        def run(x,y,draw=False):

            task.getscreen().tracer(1,0)
            task.pensize(2)
            if draw: 
                task.pendown()
            else:
                task.penup()    

            task.pencolor(color)
            task.goto(x,y)
            task.penup()

        if data==0:    
            run(150,200)
            run(290,200,True)
            run(300,210,True)
            run(300,240,True)
            run(290,250,True)

            run(240,250,True)
            runtext("logout",20,-5,-65)

            run(150,250,True)
            run(160,240,True)
            run(160,210,True)
            run(150,200,True)
        elif data==1:
            task.clear()

            #outdated momentan   function for display username
            run(0,250,False)
            #run(0,251,True)
            text=fun_txt
            runtext(text,15,45,-80)
                


            





ako.bgcolor("#03060d")
# mas=Masa_de_joc()
# mas.draw_succesful_login(1)
# mas.draw_login_menu()  


# done()

# data=mas.draw_sign_up()
# print(data)
# done()
# mas.draw_credits()

# done()
# # mas.run_draw()
# mas.draw_hitbox()
# mas.draw_hitbox([0,110],"CREDITS")
# mas.draw_hitbox([0,-110],"LOGIN")




