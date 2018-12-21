import commands
import os
import tkinter as tk 
#r = tk.Tk() 
#r.title('Counting Seconds') 
from tkinter import *
master = Tk() 
Label(master, text='Enter the URL').grid(row=0) 
e1 = Entry(master) 
e1.grid(row=0, column=1)
Label(master, text='Name The Database of which the table you want to see').grid(row=1)
e2 = Entry(master) 
e2.grid(row=1, column=1)  
Label(master, text='Enter the name of table').grid(row=2)
e3 = Entry(master) 
e3.grid(row=2, column=1) 
Label(master, text='Enter the name of table').grid(row=3)
e4= Entry(master) 
e4.grid(row=3, column=1)   
def say_hi(): # you can rename 'event' to anything you want
    c1=e1.get()	
    b="sqlmap -u "
    g=" --dbs"
    c=b+c1+g
    o = commands.getoutput(c)
    r = o.find('database') 
    l=len(o)
    g=(o[r:l])
    #print g
    Label(master, text = g).grid(row=6)
def table():
	c2=e2.get()
	c1=e1.get()	
	t1=" -D "
	t3=" --tables"
	b="sqlmap -u "
	g=" --dbs"
	c=b+c1+g
	t3=c+t1+c2+t3
	o = commands.getoutput(t3)
	r = o.find('tables') 
	l=len(o)
	g=(o[r:l])
	Label(master, text = g).grid(row=6)
def schema():
	c1=e1.get()
	c2=e2.get()
	c3=e3.get()
	f3=" -T "
	f1="-D "
	f4=" --columns"
	b="sqlmap -u "
	g=" --dbs"
	#c=b+a+g
	e=b+c1
	c5=e+f1+c2+f3+c3+f4
	o=commands.getoutput(c5)
	r = o.find('+') 
	l=len(o)
	g=(o[r:l])
	Label(master, text = g).grid(row=6)
def column():
	c1=e1.get()
	c2=e2.get()
	c3=e3.get()
	c4=e4.get()
	f3=" -T "
	t1="-D "
	f4=" -C "
	f7=" --dump"
	b="sqlmap -u "
	g=" --dbs"
	e=b+c1
	c5=e+t1+c2+f3+c3+f4+c4+f7
	o=commands.getoutput(c5)
	r = o.find('+') 
	l=len(o)
	g=(o[r:l])
	Label(master, text = g).grid(row=6)
	
	


button = tk.Button(master, text='Show Database', width=25, command=say_hi).grid(row=4)
button2 = tk.Button(master, text='Tables', width=25, command=table).grid(row=4,column=1)
button3 = tk.Button(master, text='Schema', width=25, command=schema).grid(row=4,column=2)
button4 = tk.Button(master, text='Column', width=25, command=column).grid(row=4,column=3)
master.mainloop() 

