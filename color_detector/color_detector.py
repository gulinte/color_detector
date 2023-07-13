import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from colorthief import ColorThief
import os

root=Tk()
root.title("Color Detector")
root.geometry("800x470+100+100")
root.configure(bg="#F7FFE5")
root.resizable(False,False)

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Image File", filetype=(('PNG file','*.png'),
                                                                             ('JPG file','*.jpg'),
                                                                             ("ALL file",'*.txt')))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lb1.configure(image=img,width=310,height=270)
    lb1.image=img

def Findcolor():
    ct=ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    rgb1=palette[0]
    rgb2=palette[1]
    rgb3=palette[2]
    rgb4=palette[3]
    rgb5=palette[4]
    rgb6=palette[5]
    rgb7=palette[6]
    rgb8=palette[7]
    rgb9=palette[8]
    rgb10=palette[9]

    color1=f"#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    color2=f"#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    color3=f"#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    color4=f"#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    color5=f"#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    color6=f"#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    color7=f"#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    color8=f"#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    color9=f"#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    color10=f"#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"

    colors.itemconfig(id1, fill=color1)
    colors.itemconfig(id2, fill=color2)
    colors.itemconfig(id3, fill=color3)
    colors.itemconfig(id4, fill=color4)
    colors.itemconfig(id5, fill=color5)

    colors2.itemconfig(id6, fill=color6)
    colors2.itemconfig(id7, fill=color7)
    colors2.itemconfig(id8, fill=color8)
    colors2.itemconfig(id9, fill=color9)
    colors2.itemconfig(id10, fill=color10)

    hex1.config(text=color1)
    hex2.config(text=color2)
    hex3.config(text=color3)
    hex4.config(text=color4)
    hex5.config(text=color5)
    hex6.config(text=color6)
    hex7.config(text=color7)
    hex8.config(text=color8)
    hex9.config(text=color9)
    hex10.config(text=color10)
    

#app icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

Label(root,width=120,height=10,bg="#C4D7B2").pack()

frame=Frame(root,width=700,height=370,bg="white")
frame.place(x=50,y=50)

#resized icon
img=(Image.open("icon.png"))

resized_image= img.resize((60,60))
new_image= ImageTk.PhotoImage(resized_image)

Label(frame,image=new_image,bg="white").place(x=10,y=10)

Label(frame,text="Color Detector", font="arial 25 bold",bg="white", fg="#A0C49D").place(x=85,y=20)

#colors1
colors=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
colors.place(x=20,y=90)

id1=colors.create_rectangle((10,10,50,50),fill="#C4D7B2")
id2=colors.create_rectangle((10,50,50,100),fill="#411530")
id3=colors.create_rectangle((10,100,50,150),fill="#D1512D")
id4=colors.create_rectangle((10,150,50,200),fill="#F5C7A9")
id5=colors.create_rectangle((10,200,50,250),fill="#F5E8E4")

hex1=Label(colors,text="#c4d7b2",fg="#000",font="arial 12",bg="white")
hex1.place(x=60,y=20)
hex2=Label(colors,text="#411530",fg="#000",font="arial 12",bg="white")
hex2.place(x=60,y=70)
hex3=Label(colors,text="#d1512d",fg="#000",font="arial 12",bg="white")
hex3.place(x=60,y=120)
hex4=Label(colors,text="#f5c7a9",fg="#000",font="arial 12",bg="white")
hex4.place(x=60,y=170)
hex5=Label(colors,text="#f5e8e4",fg="#000",font="arial 12",bg="white")
hex5.place(x=60,y=220)

#colors2
colors2=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
colors2.place(x=180,y=90)

id6=colors2.create_rectangle((10,10,50,50),fill="#FFE6E6")
id7=colors2.create_rectangle((10,50,50,100),fill="#F2D1D1")
id8=colors2.create_rectangle((10,100,50,150),fill="#DAEAF1")
id9=colors2.create_rectangle((10,150,50,200),fill="#C6DCE4")
id10=colors2.create_rectangle((10,200,50,250),fill="#898AA6")

hex6=Label(colors2,text="#ffe6e6",fg="#000",font="arial 12",bg="white")
hex6.place(x=60,y=20)
hex7=Label(colors2,text="#f2d1d1",fg="#000",font="arial 12",bg="white")
hex7.place(x=60,y=70)
hex8=Label(colors2,text="#daeaf1",fg="#000",font="arial 12",bg="white")
hex8.place(x=60,y=120)
hex9=Label(colors2,text="#c6dce4",fg="#000",font="arial 12",bg="white")
hex9.place(x=60,y=170)
hex10=Label(colors2,text="#898aa6",fg="#000",font="arial 12",bg="white")
hex10.place(x=60,y=220)

#image selection
selectimage=Frame(frame,width=340,height=350,bg="#C4D7B2")
selectimage.place(x=350,y=10)

f=Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lb1=Label(f,bg="black")
lb1.place(x=10,y=0)

Button(selectimage,text="Select Image", width=12,height=1,font="arial 12", command=showimage).place(x=40,y=300)
Button(selectimage,text="Find Colors", width=12,height=1,font="arial 12", command=Findcolor).place(x=185,y=300)

root.mainloop()
