#!/usr/bin/env python
'''
GUI for Socket Chat Room
'''

#coding: UTF-8 
from Tkinter import * 

def resize(ev=None):
	label.config(font='Helvetic -%d bold'%scale.get())




#window
top = Tk() 
top.geometry('600x800')

#label
label = Label(top,text="Chat Room",font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)

#button 
quit = Button(top,text="QUIT", command=top.quit,fg='white',bg='red')
quit.pack(fill=X, expand = 1) 

#scale 
scale = Scale(top, from_=10, to=50, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X,expand=2)


mainloop() 





