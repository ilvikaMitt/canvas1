from tkinter import*
from PIL import ImageTk,Image
root=Tk()

root.geometry("600x600")
root.title("canvas")

color=Label(root,text="Enter color")
color.place(relx=0.6,rely=0.9,anchor=CENTER)

color_input=Entry(root)
color_input.insert(0,"green")
color_input.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=590,height=510,background="white",highlightbackground="lightgrey")
canvas.pack()

start_img=ImageTk.PhotoImage(Image.open("start_point1.png"))
myImage=canvas.create_image(50,50,image=start_img)

direction=""
old_x=50
old_y=50
new_x=50
new_y=50

def right_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_x=new_x+5
    direction="Right"
    draw(direction,old_x,old_y,new_x,new_y)
    
def left_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_x=new_x-5
    direction="Left"
    draw(direction, old_x, old_y, new_x, new_y)

def up_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_y=new_y-5
    direction="Up"
    draw(direction, old_x, old_y, new_x, new_y)

def down_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_y=new_y+5
    direction="Down"
    draw(direction, old_x, old_y, new_x, new_y)
    
    
    

def draw(direction,old_x,old_y,new_x,new_y):
    fill_color=color_input.get()
    if (direction=="Right"):
        right_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
        
    if (direction=="Left"):
        left_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
        
    if (direction=="Up"):
        up_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
        
    if (direction=="Down"):
        down_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
        
 
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Down>",down_dir)    
root.bind("<Up>",up_dir)

    

root.mainloop()