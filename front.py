from tkinter import Tk,ttk,Label,Button,Entry,IntVar,Checkbutton,END,PhotoImage
from Passgen import *
from qr import *
import os
scriptdir=os.path.abspath(__file__)
os.chdir(scriptdir.removesuffix('/front.py'))

window = Tk()  
window.geometry("350x280")
window.resizable(width=False, height=False)
window.configure(background="#ccc")
ttk.Style().configure("TCheckbutton", padding=6, relief="flat",
   background="#ccc")
ttk.Style().configure("TEntry", relief="flat")
window.title("Passgen by anqude")  
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./icon.png'))
ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")
   
label = Label(text="Passgen") 
label.configure(background="#ccc", font=("", 20))

counter=8
button = ttk.Button(text="Generate!",width = 39)
genqr = ttk.Button(text="Generate qr code!",width = 39)





def copy_click(event):
    name = entry.get()
    pass_copy(True,name)

def handle_click(event):
    entry.delete(0, END)
    try:
      password=pass_generate(Checkvariables(),int(label2.get()))
      entry.insert(0, password)
    except:
       entry.insert(0, "") 
   
def genadiy(event):
    generate_qr(entry.get())
    os.system("python3 ./qrview.py") 

def plus_click(event):
    global counter
    counter=int(label2.get())
    counter+=1
    label2.delete(0, END)
    label2.insert(0, counter)
def minus_click(event):
    global counter
    counter=int(label2.get())
    if counter==1:
      pass
    else:
      counter-=1 
    label2.delete(0, END)
    label2.insert(0, counter)
def Checkvariables():
    
    password_lst=alph_generate(Chnumber.get(),ChletterB.get(),ChletterS.get(),Chspec.get())
    return password_lst
Chspec = IntVar()
ChletterB = IntVar()
ChletterS = IntVar()
Chnumber = IntVar()


button.bind("<Button-1>", handle_click)
genqr.bind("<Button-1>", genadiy)

entry = ttk.Entry(width = 40)
CheckCpec = Checkbutton(text='Special',variable=Chspec, onvalue=True, offvalue=False, command=Checkvariables,background='#ccc')
CheckLetterB = Checkbutton(text='LETTERS',variable=ChletterB, onvalue=True, offvalue=False, command=Checkvariables,background='#ccc')
CheckLetterS = Checkbutton(text='Letters',variable=ChletterS, onvalue=True, offvalue=False, command=Checkvariables,background='#ccc')
CheckNumber = Checkbutton(text='Number',variable=Chnumber, onvalue=True, offvalue=False, command=Checkvariables,background='#ccc')
CheckNumber.select()

plus = ttk.Button(text="+")
plus.bind("<Button-1>", plus_click)
minus = ttk.Button(text="-")
minus.bind("<Button-1>", minus_click)
Copy = ttk.Button(text="Copy!",width = 39)
Copy.bind("<Button-1>", copy_click)
label2 = ttk.Entry(width = 4) 
label2.insert(0, counter)

label.pack(anchor="nw")


entry.place(x=14, y=35)
button.place(x=12, y=65)

CheckCpec.place(x=12, y=110)
CheckLetterB.place(x=92, y=110)
CheckLetterS.place(x=182, y=110)
CheckNumber.place(x=262, y=110)
label2.place(x=157, y=150)
minus.place(x=12, y=140)
plus.place(x=252, y=140)
Copy.place(x=12, y=190)
genqr.place(x=12, y=230)

window.mainloop()
