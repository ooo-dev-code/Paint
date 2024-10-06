from tkinter import *

# Variable

actual_x, actual_y = 0, 0
now_x, now_y = 0, 0
width_line = 1
color = "black"
draw = False
square_draw = False
  
  
# Color

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
    global actual_x, actual_y
    actual_x, actual_y = event.x, event.y
    print(actual_x, actual_y)
    
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
    else:
        canvas.create_rectangle(actual_x, actual_y, event.x, event.y, fill =color,width = 2, outline=color)

# Define new line width
def line_w(event):
    global btn_width
    global width_line
    width_line = btn_width.get()
    print(width_line)
    global line_ex_width
    line_ex_width.delete("all")
    line_ex_width.create_line(0, 25, 55, 25, fill="white", width=width_line)
    
def draw_btn():
    global draw, square_draw
    draw = True
    square_draw = False
    print(draw)
    print(square_draw)
    
def square_btn():
    global square_draw, draw
    square_draw = True
    draw = False
    print(square_draw)
    print(draw)
    
    
# Window and frame
w = Tk()

w.geometry("480x480")
w.title("Paint")
w.resizable(False, False)

title = Label(w, text="Paint", bg="black", fg="white", width=75, height=2, font=50)
title.pack()

frame = Frame(w)
frame.pack()

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

elif square_draw == True:
    canvas.bind('<Button-1>', square_pos)
    canvas.bind('<B1-Motion>', square)

btn_width.bind('<Leave>', line_w)


# Loop

w.mainloop()
