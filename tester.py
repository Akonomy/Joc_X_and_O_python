

# # # # # # mas=Masa_de_joc()
# # # # # # ak.pendown()
# # # # # # ak.color("white")
# # # # # # ak.goto(200,300)
# # # # # # time.sleep(1)

# # # # # # mas.run_draw()
# # # # # # ak.bgcolor("white")
# # # # # # ak.pendown()

# # # # # # ak.clear()
# # # # # # ak.pencolor("black")
# # # # # # ak.goto(0,10)
# # # # # # ak.goto(300,-10)


# # # # # # done()


# # # # # #testat 13/12/2022

# # # # # #result:
# # # # # """ Is working well , poate fi utilizata procedura de sus in programul principal """




# # # # # # "TASK AFTER THIS    "



# # # # # # # from grafica import*
# # # # # # from turtle import*
# # # # # # import turtle as ak


# # # # # # text=ak.Turtle()

# # # # # # text.goto(2,4)
# # # # # # text.goto(40,200)

# # # # # # ak.goto(50,23)
# # # # # # text.clear()
# # # # # # done()
# # # # # # # import time


# # # # # from  random import randint

# # # # # for x in range (1000):

# # # # # 	a=randint(1,200)
# # # # # 	b=randint(1,200)
# # # # # 	if a%b==0:
# # # # # 		print (a,":",b,"=0",a/b)


# # # # # for u in range(1000):
# # # # #         x,y=randint(-250,250),randint(-210,120)
            
# # # # #        # print(x,y)
# # # # #         ak.pendown()
# # # # #         ak.pencolor("#454545")
# # # # #         ak.pensize(1)
# # # # #         ak.goto(x,y)

# # # # #         test=["start","credits","login","outside"]
# # # # #         if getPos.mouse_to_key(x,y,"ecran_meniu")>-1:
# # # # #             #print(test[getPos.mouse_to_key(x,y,"ecran_meniu")-12])
# # # # #             ak.pencolor("green")
# # # # #         else:
# # # # #            # print(test[3])  
# # # # #             ak.pencolor("red")  

# # # # #         ak.pensize(4)
# # # # #         ak.circle(2) 
# # # # #         ak.penup()   
# # # # #     return 0



# #     # ak.speed(99999)

# #     # for u in range(500):
# #     #     x,y=randint(-300,210),randint(-220,280)
            
# #     #     choser=randint(0,3)

# #     #     test=["start","credits","login","outside"]
# #     #     if x<-190 and y<200 or x>-190 and y>170:
# #     #         if choser==1:
# #     #             x,y=randint(-300,-200),randint(190,260)
# #     #         else:
# #     #             x,y=randint(-170,190),randint(-200,200)


          
# #     #     # print(x,y)
# #     #     ak.pendown()
# #     #     ak.pencolor("#454545")
# #     #     ak.pensize(1)
# #     #     ak.goto(x,y)    

# #     #     if getPos.mouse_to_key(x,y,"ecran_login")>7:
# #     #         #print(test[getPos.mouse_to_key(x,y,"ecran_meniu")-12])
# #     #         ak.pendown()
# #     #         ak.pencolor("green")
# #     #     else:
# #     #        # print(test[3]) 
# #     #         ak.pendown() 
# #     #         ak.pencolor("red")  

# #     #     ak.pensize(4)
# #     #     ak.circle(2) 
# #     #     ak.penup()   
# #     # return 0





# # # # #      if menu_console.ismenu("ecran_credits"):

# # # # #         for u in range(400):
# # # # #             x,y=randint(-300,-50),randint(190,260)
                
# # # # #            # print(x,y)
# # # # #             ak.pendown()
# # # # #             ak.pencolor("#454545")
# # # # #             ak.pensize(1)
# # # # #             ak.goto(x,y)
# # # # #             ak.speed(9999)

           
# # # # #             if getPos.mouse_to_key(x,y,"ecran_credits")>-1:
# # # # #                 #print(test[getPos.mouse_to_key(x,y,"ecran_meniu")-12])
# # # # #                 ak.pencolor("green")
# # # # #             else:
# # # # #                # print(test[3])  
# # # # #                 ak.pencolor("red")  

# # # # #             ak.pensize(4)
# # # # #             ak.circle(2) 
# # # # #             ak.penup()   
# # # # #         return 0














# from random import randint

# letters=['q','w','e','r','t','y','u','i','o','p',
# 			  'a','s','d','f','g','h','j','k','l','z',
# 			  'x','c','v','b','n','m','0','1','2','3',
# 			  '4','5','6','7','8','9',' ','_',".","(",')','*','@',
# 			  'A','B','C','D','Q','W','R','T','Y','U','I','O','P','S','F','G','H','J','K',
# 			  'L','Z','X','C','V','N','M','~',"'",":",";"]
# cnt=0			  

# print(len(letters))				  

# sets=[]

# for x in range(300):
#     newLetters=letters.copy()
#     former=[]
#     for x in range(1000):
#         maxim=len(newLetters)-1
#         if maxim:
#             u=randint(0,maxim)
#             if newLetters[u] not in former:
#                 former.append(newLetters[u])
#                 newLetters.remove(newLetters[u])
#                 maxim=len(newLetters)-1
#         else:
#             break
#     sets.append(former)        


# for s in sets:
# 	print(s,",")









# # # # # # from random import randint

# # # # # # print(9%2)
# # # # print("Inctroduceti valoarea")
# # # # amo="trryd"


# # # # def search_in_file(message):

# # # # 	data_user=0 #struct  user pass data  0 1  

# # # # 	data_catch=[]

# # # # 	with open("logs.bin") as file:

# # # # 		for x , line in enumerate(file):
# # # # 			count=0
# # # # 			if x==data_user[0]:
# # # # 				user=self.crypt_to_message(line)
# # # # 				if user==message:
# # # # 					valid=True
# # # # 			elif valid and count<3:
# # # # 				user=self.crypt_to_message(line)
# # # # 				data_catch.append(user)
# # # # 				count+=1		

# # # # 			elif count>=2:
# # # # 				break

# # # # 			else:
# # # # 				data_user[0]+=3







	
# # # # 	file=open("logs.bin","r")
# # # # 	list_usernames=file.readlines()
# # # # 	for crypted_user in range(len(list_usernames)):
# # # # 		user=self.crypt_to_message(list_usernames[crypted_user])
# # # # 		if user==message:

# # # # 			return user,list_usernames[crypted_user+1],
# # # # 			break
# # # # 	return False



# # # # import mmap

# # # # def mmap_io_find_and_replace(filename):
# # # #     with open(filename, mode="r+", encoding="utf-8") as file_obj:
# # # #         with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
# # # #             orig_text = mmap_obj.read()
            
# # # #             new_text = orig_text.replace(b"pere",b"luggage")
# # # #             print(mmap_obj,"  +  ",new_text)
# # # #             orig_text = new_text
# # # #             mmap_obj[]=new_text
# # # #             mmap_obj.flush()




# # # # string="Akonomy"
# # # # string=string[::-1]
# # # # print(string)


# # # from turtle import*




# # # import turtle
# # # import tkinter
# # # turtle.title('Game')
# # # img = tkinter.Image("photo", file="images\\cat.png")
# # # ako._Screen._root.iconphoto(True, img)




# # # text=turtle.textinput("Password","enter the password")
# # # print(text)

# # # done()
    
# # x,xn=180,-180
# # y=160
# # z=160
# # numbers=[90,25,90,25,90,40]
# # for a in range(0,6):
# #     z-=numbers[a]
# #     if not a%2:
# #         print("if x>-180 and x<180:\n    if y<",y," and y>",z,"\n        return True")
# #     y-=numbers[a]    




# # from turtle import*
# # import turtle as ak
# # ak.ht()
# # ak.bgcolor("#03060d")


# # login=ak.Turtle()
# # login.ht()

# # login.speed(3)


# # def run(x,y,draw=False):
# #     login.pensize(2)
# #     if draw: 
# #         login.pendown()
# #     else:
# #         login.penup()    

# #     login.pencolor("cyan")
# #     login.goto(x,y)
# #     login.penup()


# # # login.pencolor("cyan")
# # # login.penup()
# # # login.goto(300,0)
# # # login.pendown()
# # # login.goto(300,250)
# # # login.goto(-300,250)
# # # login.goto(-300,-250)
# # # login.goto(300,-250)
# # # login.goto(300,250)





# # run(-180,-200,False)
# # run(-180,200,True)
# # run(180,200,True)
# # run(180,-200,True)
# # run(-180,-200,True)


# # # run(0,160)
# # # run(0,70,True)
# # # run(0,45)
# # # run(0,-45,True)
# # # run(0,-70)
# # # run(0,-160,True)



# # ##down top
# # run(-170,160)
# # run(-180,150,True)
# # run(-180,80,True)
# # run(-170,70,True) 
# # run(170,70,True)


# # ##down middle
# # run(170,45)
# # run(180,35,True)
# # run(180,-35,True)
# # run(170,-45,True)
# # run(170,-45,True)
# # run(-170,-45,True)

# # ##down bottom
# # run(-170,-70)
# # run(-180,-80,True)
# # run(-180,-150,True)
# # run(-170,-160,True)
# # run(170,-160,True)

# # ##up bottom
# # run(180,-150,True)
# # run(180,-80,True)
# # run(170,-70,True)
# # run(-170,-70,True)

# # ##up middle
# # run(-170,-45)
# # run(-180,-35,True)
# # run(-180,35,True)
# # run(-170,45,True)
# # run(170,45,True)

# # #up top
# # run(170,70)
# # run(180,80,True)
# # run(180,150,True)
# # run(170,160,True)
# # run(-170,160,True)



# # #close box


# # run(-180,200)
# # run(-290,200,True)
# # run(-300,210,True)
# # run(-300,240,True)
# # run(-290,250,True)

# # run(-180,250,True)
# # run(-190,240,True)
# # run(-190,210,True)
# # run(-180,200,True)



# # done()





####27/12/2022

# randomList=[1,2,3,4]
# a,b,c=randomList[1:4]

# print(a,b,c)


randomScore="0 9"
score=randomScore.split()
score=[int(score[0]),int(score[1])]
print(score)


TIPS=[  

        "Ai un talent incontestabil... la a face ceva din nimic.",
        "Nu-i bai, ai reusit macar sa te trezesti la timp azi.",
        "Niciodata nu esti singur cand ai probleme, intotdeauna exista cineva dispus sa-ti ofere un sfat inutil.",
        "Poti face orice iti doresti in viata, atat timp cat nu necesita abilitati sau talent.",
        "Fii mandru de tine, esti unic in felul tau. La fel ca toti ceilalti.",
        "Viata este ca o cutie de ciocolata... niciodata nu stii ce primesti, dar sigur nu e ceea ce-ti doresti.",
        "Nu-ti face griji daca iti merge greu. Daca ai stat suficient de mult pe loc, incepi sa cresti radacini.",
        "Nu te ingrijora ca esti diferit. Cand toti ceilalti sunt la fel, te poti considera special.",
        "Succesul vine la cei care isi urmaresc cu tenacitate obiectivele... sau cel putin asta le spunem copiilor.",
        "Nu te ingrijora, lucrurile se vor imbunatati. Sau nu, cine stie?",
        "Viata e o ruleta ruseasca, tine-ti capul sus si spera ca nu esti urmatorul.",
        "Lasa ca marea mai are pesti, dar tu esti in mijlocul desertului",
        "In viata mai si castigi",
        "Tu chiar stai sa citesti astea?",
        "In loc sa faci ceva productiv apesi pe butoane sa vezi ce mai pica",
        "Ha ha ha, si credeam ca o sa fie o idee buna",
        "Apasa space pentru a continua jocul",
        "In viata mai si pierzi",
        "Te iubesc",
        "Oricum si maine va fi rau, de ce iti faci griji?",
        "Depinde de tine",
        "Invata, adapteaza, devino cel mai bun",
        "Fiecare zi este o noua sansa",
        "Esti o persoana valoroasa",
        "Succesul este posibil pentru tine",
        "Sanatatea este cea mai mare bogatie",
        "Ai un viitor stralucit",
        "Oamenii te iubesc si te apreciaza",
        "Exista mereu speranta",
        "Mai sunt multe lucruri bune care vor veni",
        "Fii recunoscator pentru ceea ce ai acum",
        "Invata sa te bucuri de fiecare moment",
        "Sa fii fericit este o alegere pe care o poti face",
        "Fiecare zi este o oportunitate de a invata ceva nou",
        "Iti poti atinge obiectivele daca muncesti din greu",
        "Iubeste-te pe tine insuti si pe altii",
        "Fii deschis la noi experiente si oportunitati",       
        "Fa o diferenta pozitiva in lumea inconjuratoare",
        "Zambeste, razi si bucura-te de viata",
        "Am un noroc.. se prabuseste blocu inainte sa ajung in varfu lui",
        "Bine daca nu aveam restante era bine.. dar bineinteles ca nu s-a putut",
        "Sfantu 5",
        "Incearca, nu se stie niciodata",
        "Atata s-a putut ",]


from random import*

print(TIPS[43])     
print(randint(45,48))  