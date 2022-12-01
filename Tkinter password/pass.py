#import libraries
from tkinter import *
from time import *
from pygame import mixer
import random

#intializing variables
pass_check=Tk()
pass_check.geometry('500x300')
pass_check.title('iti nuclear station')
pass_check.configure(bg="dark olive green")
pass_var=StringVar()
name_var=StringVar()
mixer.init()

#submit function to check pass and name
def submit():
	name=name_var.get()
	password=pass_var.get()
	name_var.set("")
	pass_var.set("")
	if (name=='mohamed')&(password=='123'):
		right()
	else:
		error()

#if users enter wrong data
def error():
	mixer.music.load("alarm.mp3")
	mixer.music.play(loops=0)
	
def temp_window():
	temp_w=Toplevel()
	temp_w.geometry("300x300")
	temp_w.title("temp scale")
	temp_img=PhotoImage(file="temp.gif")
	temp_l=Label(temp_w,image=temp_img)
	temp_l.pack()
	temp_w.update()
	temp_w.mainloop()
	
def day_window():
	day_w=Toplevel()
	day_w.geometry("300x300")
	day_w.configure(bg="DarkSlateGray4")
	day_w.title("day scale")
	day_img=PhotoImage(file="sun.png")
	day_img=day_img.subsample(2,2)
	day_l=Label(day_w,image=day_img,bg="DarkSlateGray4")
	day_l.pack()
	day_w.update()
	day_w.mainloop()
	
def humidity_window():
	humidity_w=Toplevel()
	humidity_w.configure(bg="PaleGreen4")
	humidity_w.geometry("300x200")
	humidity_w.title("humidity scale")
	humidity_img=PhotoImage(file="humidity.png")
	humidity_img=humidity_img.subsample(2,2)
	humidity_l=Label(humidity_w,image=humidity_img,bg="PaleGreen4")
	humidity_l.pack()
	humidity_w.update()
	humidity_w.mainloop()	
	
	

#if user entered correct data
def right():


	window=Toplevel()
	window.configure(bg="DarkOrchid4")
	window.title('iti nuclear station')
	window.geometry('700x400')

	
	img=PhotoImage(file="alarm.png")
	img=img.subsample(2,2)
	
	def label_update():
		
		temp_label=Label(window,text=str(random.randint(20,60))+"."+str(random.randint(10,60))+'\N{DEGREE SIGN}C',font=('bond',17),bg="DarkOrchid2")
		humidity_label=Label(window,text=str(random.randint(20,60))+'.'+str(random.randint(20,60))+"%",font=('bond',17),bg="DarkOrchid2")
		temp_label.place(x=150,y=100)
		humidity_label.place(x=150,y=200)
		humidity_label.after(500,label_update)
		
	img_label=Label(window,image=img,bg="DarkOrchid4")
	temp=Button(window,text='temp    :',font=('bond',15),bd=0,bg="DarkOrchid3",command=temp_window)
	day=Button(window,text='day      :',font=('bond',15),bd=0,bg="DarkOrchid3",command=day_window)
	humidity=Button(window,text='humidity:',font=('bond',15),bd=0,bg="DarkOrchid3",command=humidity_window)
	temp_label=Label(window,text=str(random.randint(20,60))+"."+str(random.randint(10,60))+'\N{DEGREE SIGN}C',font=('bond',17),bg="DarkOrchid2")
	day_label=Label(window,text="morning",font=('bond',17),bg="DarkOrchid2")
	humidity_label=Label(window,text=str(random.randint(20,60))+'.'+str(random.randint(20,60))+"%",font=('bond',17),bg="DarkOrchid2")

	img_label.place(x=400,y=40)
	temp.place(x=30,y=100)
	temp_label.place(x=150,y=100)
	day.place(x=30,y=150)
	day_label.place(x=150,y=150)
	humidity.place(x=30,y=200)
	humidity_label.place(x=150,y=200)
	
	label_update()

	
	window.mainloop()
	
	
	

intro_label=Label(pass_check, text='ITI nuclear station',font=('bond',15),bg='olive drab')

name_label = Label(pass_check, text = 'Username', font=10,bg='olive drab')
name_entry = Entry(pass_check, text = name_var, font=10)

pass_label = Label(pass_check, text = 'Password ', font=10,bg='olive drab')
pass_entry = Entry(pass_check, text = pass_var, font=10,show='#')

submit_b=Button(pass_check,text='submit',bd=2,font=12,width=8,height=1,command=submit)

name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)

pass_label.grid(row=2, column=0)
pass_entry.grid(row=2, column=1)

submit_b.place(x=200,y=100)
intro_label.grid(row=0,column=0)
pass_check.mainloop()


