#CREATE WINDOW

from tkinter import *
import time

w = Tk()

can = Canvas(w, bg="grey")
can.pack(expand=YES)

w.mainloop()

#CREATE POINT

from tkinter import *
import time

w = Tk()

w.geometry("480x480")
w.title("Paint")
w.resizable()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

w.bind('<Motion>', motion)

def save_point():
    pass

def Line(event):
    
    can.create_line(event.x,event.y,event.x+1, event.y+1, fill="green", width=5)
    
can = Canvas(w, bg="grey")
can.pack(expand=YES)

can.bind('<Button-1>', Line)
can.bind('<Button-1>', save_point)


w.mainloop()

#CREATE LINE

#DRAW

#CREATE RECTANGLE

#CREATE CIRCLE
