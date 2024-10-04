from tkinter import *
actual_x, actual_y = 0, 0
color = []

def localistion_y_and_x(event):
    global actual_x, actual_y
    actual_x, actual_y = event.x, event.y
    print(actual_x, actual_y)
    
def addLine(event):
    global actual_x, actual_y
    print(actual_x, actual_y, event.x, event.y)
    canvas.create_line((actual_x, actual_y, event.x, event.y), fill="green")
    actual_x, actual_y = event.x, event.y
    
w = Tk()
w.geometry("480x480")
w.title("kgjr")

canvas = Canvas(w, bg="grey")
canvas.pack(expand=YES)

canvas.bind('<Button-1>', localistion_y_and_x)
canvas.bind('<B1-Motion>', addLine)

w.mainloop()
