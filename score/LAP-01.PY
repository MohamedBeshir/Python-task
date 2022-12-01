
import math
from tkinter import *
import time
from threading import *
from pygame import mixer

running = False
hours=0
minutes=0
seconds = 0
counter_m=0
counter_c=0


board=Tk()
board.title("score board")
board.geometry('380x500')
mixer.init()

def start():
	global running
	if not running:
		update()
		running = True

def update():
	global hours, minutes, seconds
	seconds += 1
	if seconds == 60:
		minutes += 1
		seconds = 0
	if minutes == 60:
		hours += 1
		minutes = 0
		
	if seconds>9:
		seconds_string=str(seconds)
	else:
		seconds_string='0'+str(seconds)
		
	if minutes>9:
		minutes_string=str(minutes)
	else:
		minutes_string='0'+str(minutes)
		
	if hours>9:
		hours_string=str(hours)
	else:
		hours_string='0'+str(hours)
		
	stopwatch_label=Label(board,text=hours_string + ':' + minutes_string + ':' + seconds_string,font=('Arial', 20))
	stopwatch_label.place(x=0,y=0)
	stopwatch_label.after(1000, update)




	
def click_mor():
	global counter_m
	counter_m=counter_m+1
	score_s="cor:"+str(counter_c)+"   mor:" +str(counter_m)
	score=Label(board , text = score_s)
	score.place(x=150,y=300)
	mixer.music.load("mor.mp3")
	mixer.music.play(loops=0)

def click_cor():
	global counter_c
	counter_c=counter_c+1
	score_s="cor:"+str(counter_c)+"   mor:" +str(counter_m)
	score=Label(board , text = score_s)
	score.place(x=150,y=300)
	mixer.music.load("cor.mp3")
	mixer.music.play(loops=0)

mor=PhotoImage(file="morroco.png")
cor=PhotoImage(file="croatia.png")

mor=mor.subsample(12,12)
cor=cor.subsample(20,20)

b1=Label(board , text = "mor")
b2=Label(board , text = "cro")

mor_1 = Label(board ,image=mor)
cor_1 = Label(board ,image=cor)

mor_b=Button(board , text = "mor",command=click_mor)
cor_b=Button(board , text = "cor",command=click_cor)

score_s="cor:"+str(counter_c)+"   mor:" +str(counter_m)
score=Label(board , text = score_s)
score.place(x=150,y=300)

mor_1.place(x=50,y=70)
cor_1.place(x=250,y=70)
b1.place(x=80,y=120)
b2.place(x=280,y=120)
mor_b.place(x=80,y=140)
cor_b.place(x=280,y=140)


stopwatch_label = Label(board,text='00:00:00', font=('Arial', 20))
stopwatch_label.place(x=0,y=0)

start_button = Button(board, text='start', height=1, width=3, command=start)
start_button.place(x=0,y=30)

quit_button = Button(board, text='quit', height=1, width=3, command=board.quit)
quit_button.place(x=30,y=30)


board.mainloop()
	











# # Program to make a simple
# # login screen

# import tkinter as tk

# root=tk.Tk()

# # setting the windows size
# root.geometry("300x100")

# # declaring string variable
# # for storing name and password
# name_var=tk.StringVar()
# passw_var=tk.StringVar()


# # defining a function that will
# # get the name and password and
# # print them on the screen
# def submit():

	# name=name_var.get()
	# password=passw_var.get()
	
	# print("The name is : " + name)
	# print("The password is : " + password)
	
	# name_var.set("")
	# passw_var.set("")
	
	
# # creating a label for
# # name using widget Label
# name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# # creating a entry for input
# # name using widget Entry
# name_entry = tk.Entry(root,text = name_var, font=('calibre',10,'normal'))

# # creating a label for password
# passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# # creating a entry for password
# passw_entry=tk.Entry(root, text = passw_var, font = ('calibre',10,'normal'), show = '@')

# # creating a button using the widget
# # Button that will call the submit function
# sub_btn=tk.Button(root,text = 'Submit', command = submit)

# # placing the label and entry in
# # the required position using grid
# # method
# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)

# # performing an infinite loop
# # for the window to display
# root.mainloop()





















# mor_b=Button(board , text = "mor",command = main_click, fg = "dark green", bg = "white").pack()
# cor_b=Button(board , text = "cor",command = main_click, fg = "dark green", bg = "white").pack()








# from tkinter import *

# calc=Tk()
# calc.title("Tiny calculator")


# calc.geometry('380x500')
# screen=Button(calc , text ="screen", fg="blue",width = 60 , height= 10 , bd=1)
# b_ln=Button(calc , text = "ln",fg ='black',width = 10, height = 3,bd=1)
# b_log=Button(calc , text = "log",fg ='black',width = 10, height = 3,bd=1)
# b_pwr=Button(calc , text = "y^x",fg ='black',width = 10, height = 3,bd=1)
# b_root=Button(calc , text = "ro",fg ='black',width = 10, height = 3,bd=1)
# b_sqpwr=Button(calc , text = "x^2",fg ='black',width = 10, height = 3,bd=1)
# b_sign=Button(calc , text = "+/-",fg ='black',width = 10, height = 3,bd=1)
# b_0=Button(calc , text = "0",fg ='black',width = 10, height = 3,bd=1)
# b_dot=Button(calc , text = ".",fg ='black',width = 10, height = 3,bd=1)
# b_1=Button(calc , text = "1",fg ='black',width = 10, height = 3,bd=1)
# b_2=Button(calc , text = "2",fg ='black',width = 10, height = 3,bd=1)
# b_3=Button(calc , text = "3",fg ='black',width = 10, height = 3,bd=1)
# b_4=Button(calc , text = "4",fg ='black',width = 10, height = 3,bd=1)
# b_5=Button(calc , text = "5",fg ='black',width = 10, height = 3,bd=1)
# b_6=Button(calc , text = "6",fg ='black',width = 10, height = 3,bd=1)
# b_7=Button(calc , text = "7",fg ='black',width = 10, height = 3,bd=1)
# b_8=Button(calc , text = "8",fg ='black',width = 10, height = 3,bd=1)
# b_9=Button(calc , text = "9",fg ='black',width = 10, height = 3,bd=1)
# b_br1=Button(calc , text = "(",fg ='black',width = 10, height = 3,bd=1)
# b_br2=Button(calc , text = ")",fg ='black',width = 10, height = 3,bd=1)
# b_fac=Button(calc , text = "n!",fg ='black',width = 10, height = 3,bd=1)
# b_divi=Button(calc , text = "1/X",fg ='black',width = 10, height = 3,bd=1)
# b_mod=Button(calc , text = "|x|",fg ='black',width = 10, height = 3,bd=1)
# b_exp=Button(calc , text = "exp",fg ='black',width = 10, height = 3,bd=1)
# b_pi=Button(calc , text = "pi",fg ='black',width = 10, height = 3,bd=1)
# b_e=Button(calc , text = "e",fg ='black',width = 10, height = 3,bd=1)
# b_clr=Button(calc , text = "ce",fg ='black',width = 10, height = 3,bd=1)
# b_del=Button(calc , text = "x",fg ='black',width = 10, height = 3,bd=1)
# b_mod1=Button(calc , text = "mod",fg ='black',width = 10, height = 3,bd=1)
# b_div=Button(calc , text = "/",fg ='black',width = 10, height = 3,bd=1)
# b_mult=Button(calc , text = "x",fg ='black',width = 10, height = 3,bd=1)
# b_minus=Button(calc , text = "-",fg ='black',width = 10, height = 3,bd=1)
# b_plus=Button(calc , text = "+",fg ='black',width = 10, height = 3,bd=1)
# b_equal=Button(calc , text = "=",fg ='black',width = 10, height = 3,bd=1)


# screen.place(x=0,y=0)
# b_ln.place(x=0 , y=150)
# b_pwr.place(x=0,y=250)
# b_root.place(x=0,y=300)
# b_sqpwr.place(x=0,y=350)
# b_log.place(x=0,y=200)
# b_fac.place(x=0,y=400)
# b_pi.place(x=0,y=450)

# b_divi.place(x=75,y=150)
# b_mod.place(x=75,y=200)
# b_br1.place(x=75,y=250)
# b_7.place(x=75,y=300)
# b_4.place(x=75,y=350)
# b_1.place(x=75,y=400)
# b_sign.place(x=75,y=450)

# b_exp.place(x=150,y=150)
# b_del.place(x=150,y=200)
# b_br2.place(x=150,y=250)
# b_8.place(x=150,y=300)
# b_5.place(x=150,y=350)
# b_2.place(x=150,y=400)
# b_0.place(x=150,y=450)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

# b_clr.place(x=225,y=150)
# b_mod1.place(x=225,y=200)
# b_e.place(x=225,y=250)
# b_9.place(x=225,y=300)
# b_6.place(x=225,y=350)
# b_3.place(x=225,y=400)
# b_dot.place(x=225,y=450)


# b_mult.place(x=300,y=250)
# b_div.place(x=300,y=300)
# b_minus.place(x=300,y=350)
# b_plus.place(x=300,y=400)
# b_equal.place(x=300,y=450)

# calc.mainloop()







# def printf():
    # print("c")

# from tkinter import* 

# window_1=Tk()
# window_1.title("hello from tkinter")


# window_1.geometry('500x200')
# photo_1=PhotoImage(file="main.png")
# photo_1=photo_1.subsample(5,5)
# b1=Button(window_1 , text = "start",command=printf,image=photo_1,background="LightBlue2")
# b2=Button(window_1 , text = "right",background="LightBlue2")
# b3=Button(window_1 , text = "left",background="SeaGreen",fg="LightBlue2")

# label_1 = Label(window_1 , text = "iti")

# b1.pack(side = TOP)
# b2.pack(side = RIGHT)
# b3.pack(side = LEFT)
# label_1.pack(side=BOTTOM)



# window_1.mainloop()








#f1=open("file.cpp","w")
#f1.write("#include <iostream> \n")
#f1.write("using namespace std; \n")
#data=input("please enter string to print")
#f1.write("int main () \n { \n")
#f1.write("  cout << \"")
#f1.write(data)
#f1.write("\"; \n}")
 









#import csv


#f1=csv.reader(open("file.csv","r"))
#dict_1={}

#for line in f1:
#    dict_1[line[0]]={'clk': line[1],'type':line[2]}


#print(dict_1)





#import asdhdkhdgshdgzxmcvqwydahgdsjhfdgqwk as new
#import BIT_MATH
#import platform

#reg=10
#x= BIT_MATH.set_bit(reg,0)
#y= new.set_bit(reg,0)


#print(dir(new))
#print(y)