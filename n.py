from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
root = Tk()
root.title("Guess the number")
Label(root,text="Number Guessing Game",font= 100,bg="black",fg="yellow",border=10).grid(row=0,column=3)
img=Image.open('1.png')
x=4
y=4
re_img = img.resize((2048//x,1316//y))
img = ImageTk.PhotoImage(re_img)
Label(image = img).grid(row=1,column=3)               
