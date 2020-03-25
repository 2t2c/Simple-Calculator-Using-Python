from tkinter import *
import tkinter.font as font

#calculator window
root = Tk()
myFont = font.Font(family="Lemon Milk")
root.title("Calculator")
root.geometry("292x630")

#input text field
e = Entry(0,width = 45,borderwidth = 5)
e.grid(row=0,column=0,padx=5,pady=5,columnspan=3)

#inputing into the text field
def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

#defining functions
def clear():
    e.delete(0, END)

def add():
    f_num= e.get()
    global fnum
    global math
    math = "addition"
    fnum = float(f_num)
    e.delete(0, END)

def sub():
    f_num= e.get()
    global fnum
    global math
    math = "subtraction"
    fnum = float(f_num)
    e.delete(0, END)

def mul():
    f_num= e.get()
    global fnum
    global math
    math = "multiplication"
    fnum = float(f_num)
    e.delete(0, END)

def div():
    f_num= e.get()
    global fnum
    global math
    math = "divison"
    fnum = float(f_num)
    e.delete(0, END)

def equal():
    snum = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0,fnum + float(snum))

    if math == "subtraction":
        e.insert(0,fnum - float(snum))

    if math == "multiplication":
        e.insert(0,fnum * float(snum))

    if math == "divison":
        e.insert(0,fnum / float(snum))


#defining buttons
button1 = Button(root,text="1",padx=32,pady=30,command = lambda : click(1))
button2 = Button(root,text="2",padx=30,pady=30,command = lambda : click(2))
button3 = Button(root,text="3",padx=30,pady=30,command = lambda : click(3))
button4 = Button(root,text="4",padx=30,pady=30,command = lambda : click(4))
button5 = Button(root,text="5",padx=30,pady=30,command = lambda : click(5))
button6 = Button(root,text="6",padx=30,pady=30,command = lambda : click(6))
button7 = Button(root,text="7",padx=30,pady=30,command = lambda : click(7))
button8 = Button(root,text="8",padx=30,pady=30,command = lambda : click(8))
button9 = Button(root,text="9",padx=30,pady=30,command = lambda : click(9))
button0 = Button(root,text="0",padx=30,pady=30,command = lambda : click(0))
buttondot = Button(root,text=".",padx=32,pady=30,command = lambda : click("."))
add = Button(root,text="+",padx=30,pady=30,command = add)
sub = Button(root,text="-",padx=31,pady=30,command = sub)
mul = Button(root,text="*",padx=32,pady=30,command = mul)
div = Button(root,text="/",padx=31,pady=30,command = div)
equal = Button(root,text="=",padx=29,pady=30,command = equal)
clear = Button(root,text="CL",padx=73,pady=30,command = clear)

#setting fonts
button1["font"] = myFont
button2["font"] = myFont
button3["font"] = myFont
button4["font"] = myFont
button5["font"] = myFont
button6["font"] = myFont
button7["font"] = myFont
button8["font"] = myFont
button9["font"] = myFont
button0["font"] = myFont
add["font"] = myFont
sub["font"] = myFont
mul["font"] = myFont
div["font"] = myFont
equal["font"] = myFont
clear["font"] = myFont
buttondot["font"] = myFont

#mapping buttons onto root layout
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
add.grid(row=4,column=1)
sub.grid(row=4,column=2)
mul.grid(row=5,column=0)
div.grid(row=5,column=1)
buttondot.grid(row=5,column=2)
equal.grid(row=6,column=2)
clear.grid(row=6,column=0,columnspan = 2)




root.mainloop()