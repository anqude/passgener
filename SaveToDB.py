from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry,BOTH,X,Y
from tkinter import PhotoImage
import os
from save import write_db
def save_pass():    
    login=login_entry.get()
    Password=Password_entry.get()
    if Password!="" and login!="":
        write_db(login,Password)
        


scriptdir=os.path.abspath(__file__)
os.chdir(scriptdir.removesuffix('/SaveToDB.py'))

window = CTk()  
window.geometry("350x180")

window.title("Passgen by anqude")  
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/icon.png'))


label1=CTkLabel(window,text="Login")
label1.pack(fill=BOTH,)

login_entry=CTkEntry(window)
login_entry.pack(fill=BOTH)

label2=CTkLabel(window,text="Password")
label2.pack(fill=BOTH)

 
Password_entry=CTkEntry(window)
Password_entry.pack(fill=BOTH)






Save_button=CTkButton(window,text="Save!", command=save_pass)
Save_button.pack(fill=BOTH, pady=10)




window.mainloop()
