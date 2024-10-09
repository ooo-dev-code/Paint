from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
from PIL import Image,ImageTk

# Variable

actual_x, actual_y = 0, 0
now_x, now_y = 0, 0
width_line = 1
color = "black"
draw = True
square_draw = False
circle_draw = False
saved = False
save_num= 0
destroy_name = False
  
# Colors
def white():
    global color
    color="white"
      
def red():
    global color
    color="red"
    
def pink():
    global color
    color="pink"
    
def violet():
    global color
    color="violet"
    
def green():
    global color
    color="green"
    
def black():
    global color
    color="black"
    
def blue():
    global color
    color="blue"
    
def orange():
    global color
    color="orange"
    
def yellow():
    global color
    color="yellow"
    
def brown():
    global color
    color="brown"

def eraser():
    global color
    color="grey"
    
    
#Function

# Clear canvas
def clear():
    global canvas
    canvas.delete("all")
    
# Start the point for drawings
def localistion_y_and_x(event):
    global actual_x, actual_y, width_line
    actual_x, actual_y = event.x, event.y
    print(actual_x, actual_y)
    if circle_draw == True:
        canvas.create_oval(actual_x+50*(width_line/10), actual_y+50*(width_line/10), event.x, event.y, fill =color,width = 2, outline=color)

# Start the point for the rectangle
def square_pos(event):
    global now_x
    global now_y
    now_x, now_y = event.x, event.y
    
    
# Add the line
def addLine(event):
    global actual_x, actual_y, draw
    global now_x
    global now_y
    print(actual_x, actual_y, event.x, event.y)
    if draw == True:
        canvas.create_line((actual_x, actual_y, event.x, event.y), fill=color, width=width_line)
        actual_x, actual_y = event.x, event.y
    if square_draw == True:
        canvas.create_rectangle(actual_x, actual_y, event.x, event.y, fill =color,width = 2, outline=color)
    else: 
        print("error")

# Define new line width
def line_w(event):
    global btn_width
    global width_line
    width_line = btn_width.get()
    print(width_line)
    global line_ex_width
    line_ex_width.delete("all")
    line_ex_width.create_line(0, 25, 55, 25, fill="white", width=width_line)

# Button to start drawing lines
def draw_btn():
    global draw, square_draw, circle_draw
    draw = True
    square_draw = False
    circle_draw = False
    print(draw)
    print(square_draw)

# Button to start drawing rectangles
def square_btn():
    global square_draw, draw, circle_draw
    square_draw = True
    draw = False
    circle_draw = False
    print(square_draw)
    print(draw)

# Button to start drawing circles
def circle_btn():
    global square_draw, draw, circle_draw
    square_draw = False
    draw = False
    circle_draw = True
    print(square_draw)
    print(draw)
    print(circle_draw)

# Being sure to have saved all your progress
def You_sure():
    global saved
    if saved == False:
        global sure
        root = Tk()
        
        root.geometry("300x100")
        root.title("Sure ?")
        
        def Yes():
            global w
            w.destroy()
            root.destroy()
        def No():
            root.destroy()
            
        avertissment = Label(root, text="If you don't save, you will lose all your progress")
        avertissment.pack()
        btn_sure = Button(root, text="Yes", command=Yes)
        btn_sure.pack()
        btn_regret = Button(root, text="No", command=No)
        btn_regret.pack()
        
        root.mainloop()
    else:
        w.destroy()

# Save image
def save_image():
    global save_num
    global saved
    global name_file
    
    x = w.winfo_rootx()
    y = w.winfo_rooty()+100
    save_num = str(name_file.get())
    if save_num == "":
        name_it = Label(w, text="PLEASE, NAME THE FILE IN THE ENTRY !!!", bg="grey", fg="white")
        name_it.place(y=400, x=150)
    else:
        img = ImageGrab.grab(bbox=(x, y, x + 800, y+500)).save(f"{str(save_num)}.png")
        saved = True
      
# Window and frame
w = Tk()

w.geometry("500x500")
w.title("Paint")
w.resizable(False, False)

# Top button
frame_btn = Frame(w, background="purple", width=500, height=25)
frame_btn.pack(side=TOP)
btn1 = Button(frame_btn, text="Save", command=save_image)
btn1.pack()
name_file = Entry(frame_btn)
name_file.place(x=0)
btn1.place(x=125)
btn3 = Button(frame_btn, text="Close", command=You_sure)
btn3.pack()
btn3.place(x=375)

# Title
title = Label(w, text="Paint", bg="black", fg="white", width=75, height=2, font=50)
title.pack()

# Placement for the Canvas
frame = Frame(w)
frame.pack()

# Place to draw
canvas = Canvas(frame, bg="grey", width=450, height=300)
canvas.pack(side=RIGHT, anchor="n")

# Button

btn_clear = Button(w, text="Clear", command=clear, background="white", fg= "black", font = "underline", activebackground="black", activeforeground="red")
btn_clear.pack(anchor="n", side=RIGHT)

btn_width = Scale(w, orient=HORIZONTAL, relief="sunken", background="burlywood4", foreground="white", from_=1, to=20)
btn_width.pack(anchor="w", side=TOP)

line_ex_width = Canvas(w, bg="grey", width=50, height=50, highlightbackground="black", highlightthickness=1)
line_ex_width.pack(anchor="n", side=LEFT)
line_ex_width.create_line(0, 25, 55, 25, fill="white", width=width_line)

btn_draw = Button(w, text="Draw", command=draw_btn)
btn_draw.pack(anchor="e")
btn_square = Button(w, text="Square", command=square_btn)
btn_square.pack(anchor="e")
btn_circle = Button(w, text="Circle", command=circle_btn)
btn_circle.pack(anchor="e")

# Color Button

btn_white = Button(frame, bg="white", command=white, width=30)
btn_white.pack(anchor="w")
btn_brown = Button(frame, bg="brown", command=brown, width=30)
btn_brown.pack(anchor="w")
btn_red = Button(frame, bg="red", command=red, width=30)
btn_red.pack(anchor="w")
btn_orange = Button(frame, bg="orange", command=orange, width=30)
btn_orange.pack(anchor="w")
btn_yellow = Button(frame, bg="yellow", command=yellow, width=30)
btn_yellow.pack(anchor="w")
btn_green = Button(frame, bg="green", command=green, width=30)
btn_green.pack(anchor="w")
btn_blue = Button(frame, bg="blue", command=blue, width=30)
btn_blue.pack(anchor="w")
btn_pink = Button(frame, bg="pink", command=pink, width=30)
btn_pink.pack(anchor="w")
btn_violet = Button(frame, bg="violet", command=violet, width=30)
btn_violet.pack(anchor="w")
btn_black = Button(frame, bg="black", command=black, width=30)
btn_black.pack(anchor="w")
btn_eraser = Button(frame, bg="grey", command=eraser, width=30)
btn_eraser.pack(anchor="w")


# Bind

if square_draw == False:
    canvas.bind('<Button-1>', localistion_y_and_x)
    canvas.bind('<B1-Motion>', addLine)

btn_width.bind('<Leave>', line_w)
    
# Loop

w.mainloop()
