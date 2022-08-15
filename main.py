from tkinter import *
from tkinter import ttk
import tkinter.font as font

root = Tk()

root.title("Mel's Cool Calculator")
geo = '400x500+' + str(int(root.winfo_screenwidth() / 2) - 200) + '+' + str(int(root.winfo_screenheight() / 2) - 250)
root.geometry(geo)
root.configure(bg='#856ff8')

def numText(txt):
    answer.config(text = answer.cget('text') + txt)

def calc(eq):
    answer.config(text = str(eval(eq)))

def clear():
    answer.config(text='')

answer = Label(root, bg='gray', width='17', height='2', text='', font=("Consolas", 30))
answer.place(x=5, y=5)

buttons = []
buttons.append(ttk.Button(root, text='0', command=lambda: numText('0')))
buttons.append(ttk.Button(root, text='1', command=lambda: numText('1')))
buttons.append(ttk.Button(root, text='2', command=lambda: numText('2')))
buttons.append(ttk.Button(root, text='3', command=lambda: numText('3')))
buttons.append(ttk.Button(root, text='4', command=lambda: numText('4')))
buttons.append(ttk.Button(root, text='5', command=lambda: numText('5')))
buttons.append(ttk.Button(root, text='6', command=lambda: numText('6')))
buttons.append(ttk.Button(root, text='7', command=lambda: numText('7')))
buttons.append(ttk.Button(root, text='8', command=lambda: numText('8')))
buttons.append(ttk.Button(root, text='9', command=lambda: numText('9')))
buttons.append(ttk.Button(root, text='+', command=lambda: numText('+')))
buttons.append(ttk.Button(root, text='-', command=lambda: numText('-')))
buttons.append(ttk.Button(root, text='/', command=lambda: numText('/')))
buttons.append(ttk.Button(root, text='*', command=lambda: numText('*')))

offsetX = 50
offsetY = 50
for i in range(7):
    buttons[i].place(x=25+(offsetX * i), y=120, height=50, width=50)
for i in range(7, 14):
    buttons[i].place(x=25+(offsetX * (i - 7)), y=170, height=50, width=50)

equals = ttk.Button(root, text='=', command= lambda: calc(answer.cget("text")))
equals.place(x=150, y=250, width=100, height=100)

clear = ttk.Button(root, text='Clear', command=clear)
clear.place(x=100, y=375, width=200, height=100)

root.mainloop()