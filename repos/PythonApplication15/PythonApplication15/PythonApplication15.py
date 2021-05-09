from tkinter import *
from PIL import ImageTk, Image


myWindow = Tk()
myWindow.title("MyTitle")
myWindow.iconbitmap('C:/Users/leont/source/repos/PythonApplication19/PythonApplication15/PythonApplication15.sln')

my_img0 = ImageTk.PhotoImage(
Image.open
("exp0.png"))
my_img1 = ImageTk.PhotoImage(
Image.open
("exp1.png"))
my_img2 = ImageTk.PhotoImage(
Image.open
("exp2.png"))

imagel_list = [my_img0,my_img1,my_img2]

my_label= Label(image=my_img0)
##my_label.pack()
my_label.grid(row=0,column=0,columnspan=3)

button_back = Button(myWindow,text="<<")
button_fw= Button(myWindow,text=">>")
button_quit = Button(myWindow, text="Exit", command=myWindow.quit)

button_back.grid(row=1,column=0)
button_fw.grid(row=1,column=2)
button_quit.grid(row=1,column=1)



##button_quit.pack()

myWindow.mainloop()