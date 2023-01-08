from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry,BOTH,X,Y
from tkinter import PhotoImage
import os
from save import write_db
from graph import ggraph
graphs=""
def save_pass():    
    login=login_entry.get()
    Password=Password_entry.get()
    if Password!="" and login!="":
        write_db(login,Password)
        


scriptdir=os.path.abspath(__file__)
os.chdir(scriptdir.removesuffix('/GraphShow.py'))

window = CTk()  
window.geometry("530x180")

window.title("Passgen by anqude")  
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/icon.png'))


label1=CTkLabel(text="X",master=window)
label1.grid(row=0, column=0, padx=20, pady=10)


x_entry=CTkEntry(master=window)
x_entry.grid(row=1, column=0, padx=20, pady=10)


label2=CTkLabel(text="Y",master=window)
label2.grid(row=0, column=1, padx=20, pady=10)
 
y_entry=CTkEntry(master=window)
y_entry.grid(row=1, column=1, padx=20, pady=10)


label3=CTkLabel(text="Length",master=window)
label3.grid(row=0, column=2, padx=20, pady=10)

len_entry=CTkEntry(master=window)
len_entry.grid(row=1, column=2, padx=20, pady=10)

def gena():
    n=int(len_entry.get())
    yn=int(y_entry.get())
    xn=int(x_entry.get())
    global graphs
    graphs=ggraph(n,xn,yn)
    graph2=""
    for i in range(len(graphs)):
        graph2+=str(graphs[i]).replace("[0"," · ").replace("]","").replace("[","").replace("[0"," · ").replace(", 0"," · ").replace(",","")+"\n"
    from customtkinter import CTkToplevel
    window = CTkToplevel()
    label=CTkLabel(text=graph2,master=window)
    label.grid( row=0, column=0)


generate_button=CTkButton(command=gena, text="generate",master=window)
generate_button.grid( row=2, column=0, padx=20, pady=10)


window.mainloop()
