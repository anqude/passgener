from secrets import choice # Для безопасной генерации пароля
from pyperclip import copy# Для копирования в буфер обмена

numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lettersB=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]
lettersS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]
special=[ "!", "@", "№", "#", "$", "%", "^", "|", "&", "*", "_", "-", "=", "+", "-", "/", "(", ")", "?", "{", "}", "[", "]", "~", ">", "<", "." ]



if __name__ == "__main__":
    lineal=int(input("Длина пароля: "))
    number=input("Использовать числа? [Д/н] ")
    letterB=input("Использовать большие буквы? [Д/н] ")
    letterS=input("Использовать маленькие буквы? [Д/н] ")  
    spec=input("Использовать спец символы? [Д/н] ")
    variables=[number,letterB,letterS,spec]
    for i in range(len(variables)):
        if variables[i] =="Д":
            variables[i]=True  
        if variables[i] =="н":  
            variables[i]=False 
    number,letterB,letterS,spec=variables[0],variables[1],variables[2],variables[3]     



def alph_generate(number,letterB,letterS,spec):
    password_lst=[] # Создаём алфавит пароля
    if number==True:
        password_lst+=numbers
    if letterB==True:
        password_lst+=lettersB
    if letterS==True:
        password_lst+=lettersS
    if spec==True:
        password_lst+=special
    return password_lst   
              
def pass_generate(password_lst,lineal):
    password=[] # Создаём непосредственно пароль
    for i in range(lineal):
        password.append(choice(password_lst))
    password=''.join(password)
    return password

def pass_copy(copys,password):
    if copys==True:
        copy(password)

if __name__ == "__main__":
    password_lst=alph_generate(number,letterB,letterS,spec)
    password=pass_generate(password_lst,lineal)
    print(password)
    if(input("Скопировать в буфер обмена? [Д/н] ")=="Д") :
        copys=True
    else:
       copys=False 
    pass_copy(copys)