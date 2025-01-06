from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Loading-Page...")
#root.geometry('1575x900')
root.geometry('2000x1000')
root.configure(bg = "burlywood4")

filename=PhotoImage(file="C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\mp.png")
background_label = Label(root, image = filename,bg = "burlywood2").place(x=675,y=0)

#sidemenu
def roll():
    roota=Toplevel()
    roota.geometry('200x300')
    roota.configure(bg="#f3ba4b")
    r = random.randint(1,12)
    print(r)
    roota.geometry("+1050+326")
    rz=(172,277)
    if(r == 1):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-1.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==2):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-2.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==3):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-3.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==4):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-4.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==5):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-5.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==6):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-6.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==7):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-7.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==8):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-8.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==9):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-9.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==10):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-10.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==11):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-11.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    elif(r==12):
        image1=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\dice-12.png")
        ri1=image1.resize(rz)
        g=ImageTk.PhotoImage(ri1,master=roll)
    background_label = Label(roota, image = g,bg = "#f3ba4b")
    #background_label = Label(roota, image = g)
    #background_label.place(x=0,y=0,relwidth=1,relheight=1)  
    background_label.pack()  
    roota.mainloop()
        
round=Label(root,text="Round -  X",bg="burlywood4",font=("Arial",40)).place(x=205,y=100)
player=Label(root,text="Now : Player X",bg="burlywood4",font=("Arial",40)).place(x=150,y=175)
roll=Button(root,text="       Roll       ",command=roll,bg="burlywood2",font=("Arial",30)).place(x=215,y=350)
next=Button(root,text="      Next      ",command=roll,bg="burlywood2",font=("Arial",30)).place(x=215,y=450)

image=Image.open("C:\\Users\\ramab\\OneDrive\\Desktop\\PES\\ALIBI FORSAKEN\\cards.png")
ri=image.resize((100,162))
c=ImageTk.PhotoImage(ri)

w1=101
h1=164

h2=1
w2=1

C1=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i1=C1.create_image(h2,w2,image=c,anchor=NW)
C1.place(x=50,y=600)
C2=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i2=C2.create_image(h2,w2,image=c,anchor=NW)
C2.place(x=200,y=600)
C3=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i3=C3.create_image(h2,w2,image=c,anchor=NW)
C3.place(x=350,y=600)
C4=Canvas(height=h1,width=w1,bg='black',bd=0,highlightthickness=0, relief='ridge')
i4=C4.create_image(h2,w2,image=c,anchor=NW)
C4.place(x=500,y=600)


#room buttons

r3=Button(root,command=None,bg="burlywood3",height=23,width=450).place(x=1350,y=0)
r2=Button(root,command=None,bg="burlywood3",height=15,width=31).place(x=1100,y=0)
r1=Button(root,command=None,bg="burlywood3",height=13,width=49).place(x=675,y=0)

r4=Button(root,command=None,bg="burlywood3",height=11,width=38).place(x=676,y=276)
r5=Button(root,command=None,bg="burlywood3",height=11,width=38).place(x=676,y=476)
r6=Button(root,command=None,bg="burlywood3",height=16,width=32).place(x=1350,y=426)

r7=Button(root,command=None,bg="burlywood3",height=20,width=28).place(x=1050,y=325)

r8=Button(root,command=None,bg="burlywood3",height=10,width=57).place(x=675,y=725)
r9=Button(root,command=None,bg="burlywood3",height=8,width=55).place(x=1150,y=750)

#start position buttons

b=Button(root,command=None,bg="burlywood4",height=1,width=1).place(x=1055,y=1)
bb=Button(root,command=None,bg="burlywood4",height=1,width=1).place(x=676,y=227)
bbb=Button(root,command=None,bg="burlywood4",height=1,width=1).place(x=676,y=677)
bbbb=Button(root,command=None,bg="burlywood4",height=1,width=1).place(x=1105,y=759)
bbbbb=Button(root,command=None,bg="burlywood4",height=1,width=1).place(x=1510,y=376)
bbbbbb=Button(root,command=None,bg="burlywood4",height=1,width=1).place(x=1510,y=702)

#grid buttons
y1=52
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1055,y=y1)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1055,y=y1+30)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1055,y=y1+60)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1055,y=y1+90)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1055,y=y1+120)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1055,y=y1+150)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1055,y=y1+180)

x1=722
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+5,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+30,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+60,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+90,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+120,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+150,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+180,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+210,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+240,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+270,y=226)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+300,y=226)

g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+5,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+30,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+60,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+90,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+120,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+150,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+180,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+210,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+240,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+270,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+300,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+330,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+360,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+390,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+420,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+450,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+480,y=676)
g2=Button(root,height=1,width=1,command=None,bg="red").place(x=x1+510,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+540,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+570,y=676)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x1+597,y=676)

y2=875
'''
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1097,y=y2-30)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1097,y=y2-55)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1097,y=y2-85)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1097,y=y2-115)
'''
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1105,y=y2-145)

#g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1105,y=y2-170)

x2=1100
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+30,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+60,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+90,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+120,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+150,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+180,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+210,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+240,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+270,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+300,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+330,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+360,y=702)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x2+390,y=702)
y3=256
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+30)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+60)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+90)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+120)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+150)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+180)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+210)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+240)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+270)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+300)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+330)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=979,y=y3+360)
g1=Button(root,height=1,width=1,command=None,bg="red").place(x=979,y=y3+390)

g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3)
g1=Button(root,height=1,width=1,command=None,bg="red").place(x=1008,y=y3+30)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+60)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+90)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+120)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+150)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+180)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+210)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+240)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+270)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+300)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+330)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+360)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=1008,y=y3+390)
x4=1279
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+30)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+60)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+90)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+120)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+150)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+180)
g1=Button(root,height=1,width=1,command=None,bg="red").place(x=x4,y=y3+210)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+240)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+270)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+300)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+330)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+360)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x4,y=y3+390)
x5=1308
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+30)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+60)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+90)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+120)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+150)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+180)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+210)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+240)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+270)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+300)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+330)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+360)
g1=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x5,y=y3+390)
x6=1040
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6,y=251)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6+30,y=251)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6+60,y=251)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6+90,y=251)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6+120,y=251)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6+150,y=251)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6+180,y=251)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x6+210,y=251)
x7=1040
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7,y=278)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7+30,y=278)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7+60,y=278)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7+90,y=278)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7+120,y=278)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7+150,y=278)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7+180,y=278)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x7+210,y=278)
x8=1040
y4=650
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8,y=y4)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8+30,y=y4)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8+60,y=y4)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8+90,y=y4)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8+120,y=y4)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8+150,y=y4)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8+180,y=y4)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x8+210,y=y4)
y5=376
x9=1340
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x9,y=y5)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x9+30,y=y5)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x9+60,y=y5)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x9+90,y=y5)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x9+120,y=y5)
g2=Button(root,height=1,width=1,command=None,bg="burlywood2").place(x=x9+150,y=y5)

root.mainloop()
