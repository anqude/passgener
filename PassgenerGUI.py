from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry,CTkCheckBox,CTkToplevel
from PassgenCLI import *
from tkinter import IntVar,END,PhotoImage
from qr import generate_qr
import os

counter=8

def Checkvariables():    
    password_lst=alph_generate(Chnumber.get(),ChletterB.get(),ChletterS.get(),Chspec.get())
    return password_lst


scriptdir=os.path.abspath(__file__)
os.chdir(scriptdir.removesuffix('/PassgenerGUI.py'))

window = CTk()  
window.geometry("350x180")
window.resizable(width=False, height=False)

window.title("Passgen by anqude")  
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/icon.png'))

label = CTkLabel(text="Passgen")
label.pack()


entry=CTkEntry(width = 320)
entry.place(x=14, y=35)


Chspec = IntVar()
CheckCpec = CTkCheckBox(text='@~#',variable=Chspec, onvalue=True, offvalue=False)
CheckCpec.place(x=14, y=70)

ChletterB = IntVar()
CheckLetterB = CTkCheckBox(text='A-Z',variable=ChletterB, onvalue=True, offvalue=False)
CheckLetterB.place(x=94, y=70)

ChletterS = IntVar()
CheckLetterS = CTkCheckBox(text='a-z',variable=ChletterS, onvalue=True, offvalue=False)
CheckLetterS.place(x=174, y=70)

Chnumber = IntVar()
CheckNumber = CTkCheckBox(text='0-9',variable=Chnumber, onvalue=True, offvalue=False)
CheckNumber.select()
CheckNumber.place(x=254, y=70)

def minus_click():
    global counter
    counter=int(label2.get())
    if counter==1:
      pass
    else:
      counter-=1 
    label2.delete(0, END)
    label2.insert(0, counter)
minus = CTkButton(text="-",command=minus_click,width = 27)
minus.place(x=12, y=100)


label2=CTkEntry(width = 40)
label2.insert(0, counter)
label2.place(x=47, y=100)


def plus_click():
    global counter
    counter=int(label2.get())
    counter+=1
    label2.delete(0, END)
    label2.insert(0, counter)
plus = CTkButton(text="+",command=plus_click,width = 27)
plus.place(x=95, y=100)


def handle_click():
    entry.delete(0, END)
    try:
      password=pass_generate(Checkvariables(),int(label2.get()))
      entry.insert(0, password)
    except:
       entry.insert(0, "") 
button=CTkButton(text="Generate pass!", command=handle_click,width = 39)
button.place(x=12, y=140)


def copy_click():
    name = entry.get()
    pass_copy(True,name)
Copy = CTkButton(text="Copy!",command=copy_click, width = 39)
Copy.place(x=122, y=140)


def genadiy():
  generate_qr(entry.get())
  from PIL import ImageTk,Image
  window = CTkToplevel()
  window.title("QR")  
  window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='qr.png'))
  window.geometry("150x150")
  window.resizable(width=False, height=False)
  window.update_idletasks()
  width=window.winfo_width()
  height=window.winfo_height()
  img = ImageTk.PhotoImage(Image.open("qr.png").resize((width,height)),master = window)
  qr=CTkButton(window,text="",image=img,border=0,fg_color=None,hover_color=None)
  qr.pack()
genqr = CTkButton(text="Generate QR!",command=genadiy,width = 39)
genqr.place(x=175, y=140)

window.mainloop()
