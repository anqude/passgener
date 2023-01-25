from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry,CTkCheckBox,CTkTabview
from logics.generate import alph_generate,pass_generate
from tkinter import IntVar,END,PhotoImage
from logics.qr import generate_qr
import os
window=CTk()
window.title("Passgen by anqude") 
scriptdir=os.path.abspath(__file__)
os.chdir(scriptdir.removesuffix('/PassgenGUI.py'))
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/icon.png'))

tabview = CTkTabview(window)
tabview.pack(fill="both", expand=True,anchor='center')

window.geometry("350x220")
window.resizable(width=False, height=False)
tabview.add("Line") # add tab at the end
tabview.add("Graph")  # add tab at the end
tabview.set("Line")  # set currently visible tab



counter=8

def Checkvariables():    
    password_lst=alph_generate(Chnumber.get(),ChletterB.get(),ChletterS.get(),Chspec.get())
    return password_lst







entry=CTkEntry(tabview.tab("Line"),width = 320)
entry.place(x=14, y=15)


Chspec = IntVar()
CheckCpec = CTkCheckBox(tabview.tab("Line"),text='@~#',variable=Chspec, onvalue=True, offvalue=False)
CheckCpec.place(x=14, y=60)

ChletterB = IntVar()
CheckLetterB = CTkCheckBox(tabview.tab("Line"),text='A-Z',variable=ChletterB, onvalue=True, offvalue=False)
CheckLetterB.place(x=94, y=60)

ChletterS = IntVar()
CheckLetterS = CTkCheckBox(tabview.tab("Line"),text='a-z',variable=ChletterS, onvalue=True, offvalue=False)
CheckLetterS.place(x=174, y=60)

Chnumber = IntVar()
CheckNumber = CTkCheckBox(tabview.tab("Line"),text='0-9',variable=Chnumber, onvalue=True, offvalue=False)
CheckNumber.select()
CheckNumber.place(x=254, y=60)

def minus_click():
    counter=int(label2.get())
    if counter==1:
      pass
    else:
      counter-=1 
    label2.delete(0, END)
    label2.insert(0, counter)
minus = CTkButton(tabview.tab("Line"),text="-",command=minus_click,width = 27)
minus.place(x=12, y=100)


label2=CTkEntry(tabview.tab("Line"),width = 40)
label2.insert(0, counter)
label2.place(x=47, y=100)


def plus_click():
    counter=int(label2.get())
    counter+=1
    label2.delete(0, END)
    label2.insert(0, counter)
plus = CTkButton(tabview.tab("Line"),text="+",command=plus_click,width = 27)
plus.place(x=95, y=100)


def handle_click():
    entry.delete(0, END)
    try:
      password=pass_generate(Checkvariables(),int(label2.get()))
      entry.insert(0, password)
    except:
       entry.insert(0, "") 
button=CTkButton(tabview.tab("Line"),text="Generate pass!", command=handle_click,width = 39)
button.place(x=12, y=140)


def copy_click():
  from pyperclip import copy
  copy(entry.get())
Copy = CTkButton(tabview.tab("Line"),text="Copy!",command=copy_click, width = 39)
Copy.place(x=122, y=140)


def genadiy():
  generate_qr(entry.get())
  from tkinter import Toplevel,Label
  from PIL import ImageTk, Image
  window = Toplevel()
  window.geometry("200x200")
  window.configure(bg="#242424")
  window.title("QR")  
  window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='qr.png'))
  bg = ImageTk.PhotoImage(file="qr.png")
  label = Label(window,background="#242424",highlightbackground="#242424")
  label.pack(fill="both", expand=True,anchor='center')

  def resize_image(win):
    image = Image.open("qr.png")
    wide=win.width
    high=win.height
    if high < wide:
      wide=high
    else:
      high=wide
    resized = image.resize((wide, high))
    image2 = ImageTk.PhotoImage(resized)
    window.image2=image2
    label.configure(image=image2)

  window.bind("<Configure>", resize_image)
  window.mainloop()

genqr = CTkButton(tabview.tab("Line"),text="Generate QR!",command=genadiy,width = 39)
genqr.place(x=175, y=140)

from logics.graph import ggraph,anonim

label1=CTkLabel(tabview.tab("Graph"),text="X",)
label1.place(x=60, y=15)


x_entry=CTkEntry(tabview.tab("Graph"),width=100)
x_entry.place(x=14, y=45)

Label3=CTkLabel(tabview.tab("Graph"),text="Y",)
Label3.place(x=170, y=15)
 
y_entry=CTkEntry(tabview.tab("Graph"),width=100)
y_entry.place(x=125, y=45)

label3=CTkLabel(tabview.tab("Graph"),text="Length")
label3.place(x=265, y=15)

len_entry=CTkEntry(tabview.tab("Graph"),width=100)
len_entry.place(x=235, y=45)

x_entry.insert(0, 3)
y_entry.insert(0,3)
len_entry.insert(0,4)

def gena():
    n=int(len_entry.get())
    yn=int(y_entry.get())
    xn=int(x_entry.get())
    from tkinter import Canvas, Toplevel
    root = Toplevel()
    root.configure(background="#242424")
    root.title("Graph")
    root.geometry("400x400")
    resx,resy=400,400
    canvas = Canvas(root,background="#242424",highlightbackground="#242424")
    canvas.pack(fill="both", expand=True)
    a=ggraph(n, xn, yn)
    Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates=anonim(n,xn,yn,a,resx,resy)
    def draw(n,xn,yn,Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates):
        for i in range (xn): #кол-во линий
            for j in range(yn): #кол-во строк
                canvas.create_oval(Xnull_coordinates[i]-3,Ynull_coordinates[j]-3,Xnull_coordinates[i]+3,Ynull_coordinates[j]+3,width=7,fill="white",outline="#565b5e")
            
        for i in range (n-1): #Кол-во точек -1 тк это линии лол
            canvas.create_line(Xcoordinates[i], Ycoordinates[i], Xcoordinates[i+1], Ycoordinates[i+1],width=7,arrow="last",fill="white")
    draw(n,xn,yn,Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates)     
    def sizable(event):
        resx,resy = event.width, event.height
        canvas.delete("all")
        Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates=anonim(n,xn,yn,a,resx,resy)
        draw(n, xn, yn,Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates)
        
    canvas.bind('<Configure>', sizable)
    root.mainloop()


generate_button=CTkButton(tabview.tab("Graph"),command=gena, text="Generate!",width=320)
generate_button.place(x=15, y=95)

window.mainloop()
