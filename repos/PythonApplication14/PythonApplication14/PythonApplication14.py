from tkinter import *

myWindow = Tk()
myWindow.title("Expand for calculator!")
e = Entry(myWindow,width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3,padx=10, pady=10)

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_add():
     first_number = e.get()
     global f_num
     global math
     math = "addition"
     f_num = int(first_number)
     e.delete(0,END)

def button_multiply():
     first_number = e.get()
     global f_num
     global math
     math = "multiply"
     f_num = int(first_number)
     e.delete(0,END)

def button_division():
     first_number = e.get()
     global f_num
     global math
     math = "division"
     f_num = int(first_number)
     e.delete(0,END)

def button_subtraction():
     first_number = e.get()
     global f_num
     global math
     math = "subtraction"
     f_num = int(first_number)
     e.delete(0,END)

def button_equal():
    sec_number = e.get()
    e.delete(0,END)
    global sec_num
    sec_num=int(sec_number)
    if (math=="addition"):
        e.insert(0,str(f_num+sec_num))
    elif (math == "subtraction"):
        e.insert(0,str(f_num-sec_num))
    elif (math == "multiply"):
        e.insert(0,str(f_num*sec_num))
    elif (math == "division"):
        e.insert(0,str(f_num/sec_num))


button_1 = Button(myWindow,text="BOMB!",padx=38, pady=20,command=lambda: button_click(1))
button_1 = Button(myWindow,text="1",padx=40, pady=20,command=lambda: button_click(1))
button_2 = Button(myWindow,text="2",padx=40, pady=20,command=lambda: button_click(2))
button_3 = Button(myWindow,text="3",padx=40, pady=20,command=lambda: button_click(3))
button_4 = Button(myWindow,text="4",padx=40, pady=20,command=lambda: button_click(4))
button_5 = Button(myWindow,text="5",padx=40, pady=20,command=lambda: button_click(5))
button_6 = Button(myWindow,text="6",padx=40, pady=20,command=lambda: button_click(6))
button_7 = Button(myWindow,text="7",padx=40, pady=20,command=lambda: button_click(7))
button_8 = Button(myWindow,text="8",padx=40, pady=20,command=lambda: button_click(8))
button_9 = Button(myWindow,text="9",padx=40, pady=20,command=lambda: button_click(9))
button_0 = Button(myWindow,text="0",padx=40, pady=20,command=lambda: button_click(0))
button_add = Button(myWindow,text="+",bg = "yellow",padx=39, pady=20,command=button_add)
button_multiply = Button(myWindow,text="*",bg = "yellow",padx=39, pady=20,command=button_multiply)
button_subtract = Button(myWindow,text="-",bg = "yellow",padx=39, pady=20,command=button_subtraction)
button_divide = Button(myWindow,text="/",bg = "yellow",padx=39, pady=20,command=button_division)

button_equal = Button(myWindow,text="=",bg = "red",padx=91, pady=20,command=button_equal)
button_clear = Button(myWindow,text="C",bg="red",padx=79, pady=20,command=button_clear)




button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_subtract.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)


myWindow.mainloop()