from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry
from tkinter import PhotoImage
import os
from logics.graph import ggraph,anonim


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

x_entry.insert(0, 3)
y_entry.insert(0,3)
len_entry.insert(0,4)

def gena():
    n=int(len_entry.get())
    yn=int(y_entry.get())
    xn=int(x_entry.get())
    graphs=ggraph(n,xn,yn)
    graph2=""
    for i in range(len(graphs)):
        graph2+=str(graphs[i]).replace("[0"," · ").replace("]","").replace("[","").replace("[0"," · ").replace(", 0"," · ").replace(",","")+"\n"
    from tkinter import Canvas, Toplevel
    root = Toplevel()
    root.configure(background="#242424")
    root.geometry("400x400")
    canvas = Canvas(root,background="#242424",highlightbackground="#242424")
    canvas.pack(fill="both", expand=True)
    root.update_idletasks()
    resx,resy = root.winfo_width(),root.winfo_height()
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


generate_button=CTkButton(command=gena, text="generate",master=window)
generate_button.grid( row=2, column=0, padx=20, pady=10)


window.mainloop()
