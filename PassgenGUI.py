from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry,CTkCheckBox,CTkTabview,get_appearance_mode
from logics.generate import alph_generate,pass_generate
from tkinter import IntVar,END,PhotoImage
from logics.qr import generate_qr
import os
from logics.entropy import get_entopy

window=CTk()
window.title("Passgen by anqude")
window.geometry("350x220")
window.resizable(width=False, height=False) 
theme=get_appearance_mode()
if theme=="Dark":
	bg_color="#242424"
	fg_color="#dbdbdb"
else:
	fg_color="#242424"
	bg_color="#dbdbdb"

scriptdir=os.path.abspath(__file__)
os.chdir(scriptdir.removesuffix('/PassgenGUI.py'))
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/icon.png'))

tabview = CTkTabview(window)
tabview.pack(fill="both", expand=True,anchor='center')

tabview.add("Line") # add tab at the end
tabview.add("Graph")  # add tab at the end
tabview.set("Line")  # set currently visible tab



counter=8

def Checkvariables():    
		password_lst=alph_generate(Chnumber.get(),ChletterB.get(),ChletterS.get(),Chspec.get())
		return password_lst


def testVal(inStr):
    if inStr!="":
        strong=get_entopy(inStr)
        Entropy.configure(text=" Strength: "+str(strong[0])+" bits, "+strong[1])
        return True
    else:
        Entropy.configure(text=" Strength:",width = 180)
        return True


entry=CTkEntry(tabview.tab("Line"),width = 320,validate="key")
entry.configure(validatecommand = (entry.register(testVal),'%P'))
entry.pack(padx=14, pady=15, fill="x")

Entropy =CTkLabel(tabview.tab("Line"),text=" Strength: ",width = 180,anchor="w")
Entropy.place(x=135, y=100)

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
		counter=int(counter_entry.get())
		if counter==1:
			pass
		else:
			counter-=1 
		counter_entry.delete(0, END)
		counter_entry.insert(0, counter)

minus = CTkButton(tabview.tab("Line"),text="-",command=minus_click,width = 27)
minus.place(x=12, y=100)


counter_entry=CTkEntry(tabview.tab("Line"),width = 40)
counter_entry.insert(0, counter)
counter_entry.place(x=47, y=100)


def plus_click():
		counter=int(counter_entry.get())
		counter+=1
		counter_entry.delete(0, END)
		counter_entry.insert(0, counter)
plus = CTkButton(tabview.tab("Line"),text="+",command=plus_click,width = 27)
plus.place(x=95, y=100)


def generate_line():
		entry.delete(0, END)
		try:
			password=pass_generate(Checkvariables(),int(counter_entry.get()))
			entry.insert(0, password)
		except:
			 entry.insert(0, "") 
button=CTkButton(tabview.tab("Line"),text="Generate pass!", command=generate_line,width = 39)
button.place(x=12, y=140)


def copy_click():
	from pyperclip import copy
	copy(entry.get())
Copy = CTkButton(tabview.tab("Line"),text="Copy!",command=copy_click, width = 39)
Copy.place(x=122, y=140)

def genadiy():
	state=generate_qr(entry.get(),fg_color,bg_color)
	from tkinter import Toplevel,Label
	from PIL import ImageTk, Image
	if state==True:
		window = Toplevel()
		window.geometry("200x200")
		window.configure(bg=bg_color)
		window.title("QR")  
		window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='qr.png'))
		bg = ImageTk.PhotoImage(file="qr.png")
		label = Label(window,background=bg_color,highlightbackground=bg_color)
		label.pack(fill="both", expand=True,anchor='center')
		counter_loop=[0]
		def resize_image(win):
			if counter_loop[0]%3==0:
				image = Image.open("qr.png")
				size=min(win.width,win.height)
				resized = image.resize((size, size))
				image2 = ImageTk.PhotoImage(resized)
				window.image2=image2
				label.configure(image=image2)
			counter_loop.insert(0,counter_loop[0]+1)
		window.bind("<Configure>", resize_image)
		window.mainloop()
	else:
		window = Toplevel()
		window.configure(bg=bg_color)
		window.title("Warning!")
		window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/warn.png'))
		label = Label(window,background=bg_color,highlightbackground=bg_color,text="Too much data to make QR!",foreground=fg_color,font=("Monospace",16))
		label.pack(fill="both", expand=True,anchor='center')
		window.attributes('-topmost', True)
		window.update()
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
		from tkinter import Canvas, Toplevel, Label
		if not ( n<=1 or n>xn*yn):
			root = Toplevel()
			root.configure(background="#242424")
			root.title("Graph")
			root.geometry("200x200")
			root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./ui/graph.png'))
			resx,resy=400,400
			canvas = Canvas(root,background=bg_color,highlightbackground=bg_color)
			canvas.pack(fill="both", expand=True)
			while True:
				a=ggraph(n, xn, yn)
				if a!=None:
					break
			Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates=anonim(n,xn,yn,a,resx,resy)
			def draw(n,xn,yn,Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates):
					for i in range (xn): #кол-во линий
							for j in range(yn): #кол-во строк
									canvas.create_oval(Xnull_coordinates[i]-3,Ynull_coordinates[j]-3,Xnull_coordinates[i]+3,Ynull_coordinates[j]+3,width=7,fill=fg_color,outline="#565b5e")
							
					for i in range (n-1): #Кол-во точек -1 тк это линии лол
							canvas.create_line(Xcoordinates[i], Ycoordinates[i], Xcoordinates[i+1], Ycoordinates[i+1],width=7,arrow="last",fill=fg_color)
			draw(n,xn,yn,Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates)     
			def sizable(event):
					resx,resy = event.width, event.height
					canvas.delete("all")
					Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates=anonim(n,xn,yn,a,resx,resy)
					draw(n, xn, yn,Xcoordinates,Ycoordinates,Xnull_coordinates,Ynull_coordinates)
					
			canvas.bind('<Configure>', sizable)
			root.mainloop()
		else:
			root = Toplevel()
			root.configure(bg=bg_color)
			root.title("Warning!")
			root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='./ui/warn.png'))
			label = Label(root,background=bg_color,highlightbackground=bg_color,text="Incorrect length!",foreground=fg_color,font=("Monospace",16))
			label.pack(fill="both", expand=True,anchor='center')
			root.attributes('-topmost', True)
			root.update()
			root.mainloop()


generate_graph=CTkButton(tabview.tab("Graph"),command=gena, text="Generate!",width=320)
generate_graph.place(x=15, y=95)

window.mainloop()
